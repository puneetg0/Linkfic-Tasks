# CineShelf

## Overview

CineShelf is a movie-library application for people who want to keep track of the films they plan to watch and the films they have already seen. Users can create an account, manage their personal collection, search and filter movies, and track watched status. Administrators have read-only pages for viewing registered users and movies across the application.

This repository folder contains the application source. It is a learning project and is not yet certified or configured for a public production release. See [Known Issues](#known-issues) before deployment.

## Features

- User registration and sign-in with email and password.
- Protected API resources using short-lived bearer tokens.
- Personal movie library with add, view, edit, watched-status update, and delete operations.
- Search by movie title and filter by genre.
- Server-side validation for movie fields and account credentials.
- User-specific movie access enforced by the API.
- Read-only administrator views for users and all movies.
- Responsive React interface for sign-in, library, and administration.
- Interactive API exploration through FastAPI Swagger UI.

## Technology Stack

| Area | Technology |
|---|---|
| Frontend | React 19, Vite 8, Tailwind CSS 4 |
| Backend | Python 3.12, FastAPI, Pydantic, Uvicorn |
| Database | PostgreSQL, SQLAlchemy 2, psycopg 3 |
| Authentication | Signed HS256 bearer tokens; PBKDF2-SHA256 password hashing |
| Containerization | Docker, Docker Compose, Nginx |
| Testing | pytest, FastAPI TestClient, SQLite test database, Oxlint |

## Architecture

The React application runs in the user's browser. It sends HTTP requests with JSON data to the FastAPI backend. For requests that need an account, the frontend includes the signed-in user's bearer token in the `Authorization` header.

FastAPI validates incoming data, verifies the token and the user's role, and uses SQLAlchemy to read or update PostgreSQL. Each movie has an owner ID. The API uses that ID to limit regular users to their own movies; administrator endpoints separately allow authorized administrators to view all users and movies.

Passwords are stored as PBKDF2-SHA256 hashes, not as readable passwords. Access tokens expire after 30 minutes. The frontend currently keeps the token in memory, so a full page reload requires the user to sign in again.

## Project Structure

```text
Day18/
├── backend/
│   ├── app/
│   │   ├── auth.py              # Registration, password hashes, tokens, access checks
│   │   ├── database.py          # SQLAlchemy engine and request-scoped sessions
│   │   ├── main.py              # FastAPI app, CORS, health check, router setup
│   │   ├── models/
│   │   │   └── db_models.py     # SQLAlchemy database tables
│   │   ├── routes/
│   │   │   ├── movie.py         # Personal movie and genre endpoints
│   │   │   └── admin.py         # Administrator read-only endpoints
│   │   └── schemas/
│   │       ├── movie.py         # Movie input validation and response schema
│   │       └── admin.py         # Administrator response schemas
│   ├── Dockerfile
│   ├── requirements.txt         # Runtime dependencies
│   ├── requirements-dev.txt     # Runtime plus test dependencies
│   └── .env.example             # Safe backend configuration template
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # Sign-in and administrator screens
│   │   ├── components/          # Reusable interface components
│   │   ├── features/library/    # Personal movie library
│   │   └── styles/              # Shared, authentication, and library styles
│   ├── Dockerfile
│   ├── nginx.conf               # Production static-file server
│   ├── package.json
│   └── .env.example             # Frontend API URL template
├── tests/
│   ├── conftest.py              # Test import path setup
│   ├── test_api.py              # API regression tests
│   └── test_practice.py         # Python practice tests
├── docs/
│   └── API.md                   # API endpoint and request reference
└── dsapractice.py               # Earlier Python practice problems
```

The Docker Compose file for this application is in [`../Day21/docker-compose.yml`](../Day21/docker-compose.yml), and the Day 21 release-preparation notes are in [`../Day21/README.md`](../Day21/README.md).

## Prerequisites

- Python 3.12.
- Node.js 20.19 or newer (or 22.12 or newer), and npm.
- PostgreSQL 14 or newer, available to the backend.
- Git.
- Docker Desktop with its Linux container engine running, if using Docker.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/puneetg0/Linkfic-Tasks.git
```

In PowerShell, enter the project folder with:

```powershell
Set-Location Linkfic-Tasks\Day18
```

### 2. Create a PostgreSQL database

Create a database named `cineshelf` and have the database username, password, host, and port ready. For a local PostgreSQL installation, the default port is usually `5432`.

### 3. Configure and install the backend

From the `Day18` folder:

```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
```

Edit `backend/.env` and set `DATABASE_URL` to your PostgreSQL connection string and `JWT_SECRET_KEY` to a new random secret of at least 32 characters. Keep this `.env` file private; never commit real credentials or signing keys.

Example connection string format:

```text
postgresql+psycopg://db_user:db_password@localhost:5432/cineshelf
```

### 4. Configure and install the frontend

Open another terminal in the `Day18` folder:

```powershell
cd frontend
npm ci
```

The checked-in `frontend/.env.example` points the development frontend at `http://localhost:8000`. Copy it to `frontend/.env` only if you need to change the API address.

## Environment Variables

| Variable | Required | Example | Purpose |
|---|---:|---|---|
| `DATABASE_URL` | Yes | `postgresql+psycopg://db_user:db_password@localhost:5432/cineshelf` | SQLAlchemy connection string for PostgreSQL. |
| `JWT_SECRET_KEY` | Yes | `replace-with-a-new-random-secret-of-at-least-32-characters` | Private key used to sign access tokens. Use a different, randomly generated value in each environment. |
| `CORS_ORIGINS` | No for local development | `http://localhost:5173,http://127.0.0.1:5173` | Comma-separated list of trusted frontend origins allowed to call the API. For production, specify the exact HTTPS frontend origin. |
| `VITE_API_URL` | No for local development | `http://localhost:8000` | API base URL included in the frontend at build time. Set it to the deployed API URL before building. |

Safe templates are provided in [`backend/.env.example`](backend/.env.example) and [`frontend/.env.example`](frontend/.env.example). Replace example credentials before use. Vite values are embedded into public JavaScript, so never put secrets in variables prefixed with `VITE_`.

## Database Migrations

There is currently **no migration tool or migration history** in this project. When the backend starts, SQLAlchemy calls `create_all` to create missing tables. That is convenient for development, but it does not safely manage schema changes to an existing production database.

Before using a production database, add a migration workflow (for example, Alembic), create and review the initial migration, and apply migrations as a deliberate deployment step. Do not treat `create_all` as a replacement for production migrations. Back up an existing database before schema changes.

## Running the Application

### Start the backend

From `Day18/backend`, with the virtual environment activated and `.env` configured:

```powershell
python -m uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. The health endpoint is `http://localhost:8000/health`.

### Start the frontend

From `Day18/frontend` in a second terminal:

```powershell
npm run dev
```

Open `http://localhost:5173` in a browser.

## API Documentation

When the backend is running, open **[Swagger UI](http://localhost:8000/docs)** to inspect and try the live API. Open **[ReDoc](http://localhost:8000/redoc)** for an alternative generated view.

The repository's written endpoint reference is [docs/API.md](docs/API.md). It lists routes, required authentication, request examples, validation rules, and expected status codes.

## Testing

From the repository root:

```powershell
python -m pytest Day18\tests -q
```

Run this command with the Day18 backend virtual environment active. The API tests use a temporary in-memory SQLite database; they do not use or modify your PostgreSQL database.

Run the frontend checks from `Day18/frontend`:

```powershell
npm run lint
npm run build
```

## Screenshots

The screenshots below are desktop captures already included elsewhere in this repository. They show the sign-in page, movie collection, and add-movie form.

### Sign-in

![CineShelf sign-in screen](../Day20/screenshots/sign-in.png)

### Movie collection

![CineShelf movie collection](../Day20/screenshots/movie-library.png)

### Add a movie

![CineShelf add-movie form](../Day20/screenshots/add-movie.png)

The layout was checked in a browser at narrow phone, tablet, and desktop viewport widths. Separate mobile screenshot files have not yet been added.

## Known Issues

- Database schema creation currently uses SQLAlchemy `create_all`; production migrations have not been added.
- Public registration always creates a regular user. A safe administrator bootstrap procedure still needs to be designed.
- The access token is held in memory, so a page reload signs the user out.
- Login rate limiting and account recovery are not implemented.
- Docker Compose configuration is present in `Day21`, but a complete Docker image build and container run still need to be verified with Docker Engine available.
- A real staging deployment, production secrets, managed database, backups, and deployment-domain checks have not been completed.
- Existing screenshots are desktop screenshots; mobile-specific screenshots have not been captured.

## Deployment

Dockerfiles are provided for the backend and frontend. The Compose file in `Day21/docker-compose.yml` builds the `Day18` app containers and expects an existing PostgreSQL database; it does not create a database service.

1. Ensure Docker Desktop and its Linux container engine are running.
2. Copy `Day21/.env.example` to `Day21/.env`.
3. Set the real database URL and a new random JWT key. Set `CORS_ORIGINS` to the exact browser-facing frontend origin.
4. Set `VITE_API_URL` to the API address the user's browser can reach. This value is baked into the frontend at build time.
5. From the repository root, build and start the services:

   ```powershell
   docker compose --env-file Day21/.env -f Day21/docker-compose.yml up --build
   ```

6. Verify the frontend, `GET /health`, authentication, and movie operations in the deployed environment.
7. Stop local containers with:

   ```powershell
   docker compose --env-file Day21/.env -f Day21/docker-compose.yml down
   ```

For a public release, use HTTPS, store secrets in the hosting provider's secret manager, configure a managed PostgreSQL database and backups, apply reviewed database migrations, and verify the actual frontend/API domains. Do not deploy with the example values.

## Future Improvements

- Add Alembic migrations and a tested database upgrade/rollback process.
- Create a secure, documented administrator bootstrap command or deployment process.
- Add login throttling and a password-reset/account-recovery flow.
- Improve token/session behavior while following the chosen browser security model.
- Automate backend tests, frontend lint/build, and Docker builds in CI.
- Add integration tests against PostgreSQL in addition to SQLite unit/API tests.
- Capture and maintain current desktop and mobile screenshots.
- Add accessibility checks and broader browser/device testing.
- Deploy to staging, verify database backups and restore procedures, then document the release process.
