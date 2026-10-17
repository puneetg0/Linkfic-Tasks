from contextlib import asynccontextmanager
import os

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from .auth import AuthBase, router as auth_router
from .database import engine, get_db
from .routes.admin import router as admin_router
from .routes.movie import router as movie_router


CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]
if not CORS_ORIGINS:
    raise RuntimeError("Set CORS_ORIGINS to at least one trusted frontend origin.")


@asynccontextmanager
async def lifespan(_: FastAPI):
    AuthBase.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="CineShelf API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.get("/health")
def health_check(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ok"}


app.include_router(movie_router)
app.include_router(admin_router)
app.include_router(auth_router)
