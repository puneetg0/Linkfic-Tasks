import os
import sys
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite://"
os.environ["JWT_SECRET_KEY"] = "test-only-secret-key-with-at-least-32-bytes"

BACKEND_PATH = Path(__file__).resolve().parents[1] / "backend"
sys.path.insert(0, str(BACKEND_PATH))

import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.auth import (
    AuthBase,
    User,
    create_access_token,
    get_token_email,
    verify_password,
)
from app.database import get_db
from app.main import health_check
from app.routes.admin import router as admin_router
from app.routes.movie import router as movie_router


test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSession = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)


@pytest.fixture
def client():
    AuthBase.metadata.drop_all(bind=test_engine)
    AuthBase.metadata.create_all(bind=test_engine)

    api = FastAPI()
    api.add_api_route("/health", health_check)
    api.include_router(movie_router)
    api.include_router(admin_router)
    from app.auth import router as auth_router

    api.include_router(auth_router)

    def override_get_db():
        with TestSession() as db:
            yield db

    api.dependency_overrides[get_db] = override_get_db
    with TestClient(api) as test_client:
        yield test_client
    api.dependency_overrides.clear()


def register(client: TestClient, email: str, password: str = "correct-horse-123"):
    return client.post(
        "/auth/register",
        json={"email": email, "password": password},
    )


def login(client: TestClient, email: str, password: str = "correct-horse-123"):
    response = client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def movie_payload(**overrides):
    return {
        "title": "Arrival",
        "genre": "Science Fiction",
        "release_year": 2016,
        "rating": 8.0,
        "watched": False,
        "poster_url": None,
        **overrides,
    }


def test_register_login_and_read_current_user(client):
    response = register(client, "  MOVIE-LOVER@example.com  ")

    assert response.status_code == 201
    assert response.json()["email"] == "movie-lover@example.com"
    assert response.json()["role"] == "user"

    token = login(client, "MOVIE-LOVER@example.com")
    current_user = client.get("/auth/me", headers=auth_headers(token))

    assert current_user.status_code == 200
    assert current_user.json()["email"] == "movie-lover@example.com"
    assert current_user.json()["role"] == "user"


def test_registration_rejects_invalid_credentials_and_duplicate_email(client):
    assert register(client, "not-an-email").status_code == 422
    assert register(client, "short-password@example.com", "short").status_code == 422

    assert register(client, "same@example.com").status_code == 201
    duplicate = register(client, "SAME@example.com")
    assert duplicate.status_code == 409

    bad_login = client.post(
        "/auth/login",
        json={"email": "same@example.com", "password": "wrong-password"},
    )
    assert bad_login.status_code == 401


def test_protected_endpoints_reject_missing_and_invalid_tokens(client):
    assert client.get("/auth/me").status_code == 401
    assert client.get("/movies").status_code == 401
    assert client.get(
        "/auth/me",
        headers=auth_headers("not.a.valid-token"),
    ).status_code == 401


def test_movie_validation_and_crud(client):
    register(client, "owner@example.com")
    token = login(client, "owner@example.com")
    headers = auth_headers(token)

    invalid = client.post(
        "/movies",
        headers=headers,
        json=movie_payload(title="   "),
    )
    assert invalid.status_code == 422

    invalid_year = client.post(
        "/movies",
        headers=headers,
        json=movie_payload(release_year=1800),
    )
    assert invalid_year.status_code == 422

    invalid_rating = client.post(
        "/movies",
        headers=headers,
        json=movie_payload(rating=10.1),
    )
    assert invalid_rating.status_code == 422

    invalid_poster = client.post(
        "/movies",
        headers=headers,
        json=movie_payload(poster_url="javascript:alert(1)"),
    )
    assert invalid_poster.status_code == 422

    created = client.post("/movies", headers=headers, json=movie_payload())
    assert created.status_code == 201
    movie_id = created.json()["id"]
    assert created.json()["owner_id"] == 1

    assert client.get(f"/movies/{movie_id}", headers=headers).status_code == 200
    assert client.get("/genres", headers=headers).json() == ["Science Fiction"]
    assert client.get("/movies?search=arr", headers=headers).json()[0]["id"] == movie_id

    updated = client.put(
        f"/movies/{movie_id}",
        headers=headers,
        json=movie_payload(title="Arrival (updated)"),
    )
    assert updated.status_code == 200
    assert updated.json()["title"] == "Arrival (updated)"

    watched = client.patch(
        f"/movies/{movie_id}/watched",
        headers=headers,
        json={"watched": True},
    )
    assert watched.status_code == 200
    assert watched.json()["watched"] is True

    deleted = client.delete(f"/movies/{movie_id}", headers=headers)
    assert deleted.status_code == 204
    assert client.get(f"/movies/{movie_id}", headers=headers).status_code == 404


def test_users_cannot_access_each_others_movies_and_admin_routes_are_restricted(client):
    register(client, "first@example.com")
    first_token = login(client, "first@example.com")
    movie = client.post(
        "/movies",
        headers=auth_headers(first_token),
        json=movie_payload(),
    ).json()

    register(client, "second@example.com")
    second_token = login(client, "second@example.com")
    second_headers = auth_headers(second_token)

    assert client.get("/movies", headers=second_headers).json() == []
    assert client.get(
        f"/movies/{movie['id']}",
        headers=second_headers,
    ).status_code == 404
    assert client.get("/admin/users", headers=second_headers).status_code == 403
    assert client.get("/admin/movies", headers=second_headers).status_code == 403

    with TestSession() as db:
        db.execute(
            update(User)
            .where(User.email == "second@example.com")
            .values(role="admin")
        )
        db.commit()

    admin_token = login(client, "second@example.com")
    admin_headers = auth_headers(admin_token)
    assert client.get("/admin/users", headers=admin_headers).status_code == 200
    admin_movies = client.get("/admin/movies", headers=admin_headers)
    assert admin_movies.status_code == 200
    assert admin_movies.json()[0]["owner_email"] == "first@example.com"


def test_password_verifier_rejects_corrupt_or_excessive_iteration_hashes():
    assert verify_password("a-password", "not-a-password-hash") is False
    assert (
        verify_password(
            "a-password",
            "pbkdf2_sha256$999999999999999999999999$YWJj$YWJj",
        )
        is False
    )
    assert (
        verify_password(
            "a-password",
            "pbkdf2_sha256$1$YWJj$YWJj",
        )
        is False
    )


def test_health_endpoint_checks_database_connection(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_expired_signed_token_is_rejected():
    from unittest.mock import patch

    with patch("app.auth.time.time", return_value=1_000):
        token = create_access_token("expired@example.com")
    with patch("app.auth.time.time", return_value=1_000 + 31 * 60):
        with pytest.raises(HTTPException) as error:
            get_token_email(token)

    assert error.value.status_code == 401
