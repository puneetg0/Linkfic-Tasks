# CineShelf

A full-stack movie collection manager for building a personal library, tracking watched films, and finding movies by title or genre.

**Live app:** [cineshelf-frontend-5qiq.onrender.com](https://cineshelf-frontend-5qiq.onrender.com/)

## Screenshots

### Sign-in screen

![CineShelf sign-in screen](screenshots/sign-in.png)

### Add a movie

![Add movie form on the CineShelf dashboard](screenshots/add-movie.png)

### Movie collection

![Movie collection with search, genre filter, ratings, and watched status](screenshots/movie-library.png)

## Features

- Register an account and sign in with an email and password.
- Add, edit, and delete movies in your personal library.
- Record each movie's genre, release year, rating, watched status, and optional poster URL.
- Search by movie title, filter by genre, and view a list of movies still to watch.
- View and manage all users and movies with an administrator account.
- Use the FastAPI-generated interactive API documentation during development.

## Technology

| Area | Tools |
|---|---|
| Frontend | React 19, Vite 8, Tailwind CSS 4 |
| Backend | Python, FastAPI, Pydantic, Uvicorn |
| Database | PostgreSQL, SQLAlchemy 2, psycopg 3 |
| Authentication | Bearer JWT (HS256), PBKDF2-SHA256 password hashing |
| Hosting | Render |

## Project structure

The application source lives in `Day18/` in this repository. Generated folders such as `.venv`, `node_modules`, and `__pycache__` are omitted below.

```text
Day18/
├── backend/
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       ├── main.py                 # FastAPI app, CORS, and router setup
│       ├── auth.py                 # Registration, login, JWT, and user model
│       ├── database.py             # PostgreSQL engine and session dependency
│       ├── models/
│       │   ├── __init__.py
│       │   └── db_models.py        # SQLAlchemy movie model
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── movie.py            # Movie and genre endpoints
│       │   └── admin.py            # Administrator endpoints
│       └── schemas/
│           ├── __init__.py
│           ├── movie.py            # Movie request and response schemas
│           └── admin.py            # Administrator response schemas
├── frontend/
│   ├── .env.example                # Frontend API URL example
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx                 # Authentication and admin screens
│       ├── main.jsx                # React entry point
│       ├── components/
│       │   └── MovieCard.jsx       # Reusable movie card
│       ├── features/
│       │   └── library/
│       │       └── MovieLibrary.jsx # Personal library and movie actions
│       └── styles/
│           ├── index.css
│           ├── auth.css
│           └── library.css
├── tests/
│   └── test_practice.py            # Tests for Python practice functions
├── dsapractice.py
├── .gitignore
├── README.docs                    # Day 18 learning and refactoring notes
└── README.md
```

## Run locally

### Prerequisites

- Python 3.11 or newer
- Node.js 20.19+ (or 22.12+) and npm
- PostgreSQL, with a database created for CineShelf
- Git

### 1. Get the project

```powershell
git clone https://github.com/puneetg0/Linkfic-Tasks.git
cd Linkfic-Tasks\Day18
```

If you already have the repository, change to its `Day18` directory.

### 2. Configure and start the backend

Create a `backend\.env` file. This file is local and must not be committed.

```dotenv
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@localhost:5432/cineshelf
JWT_SECRET_KEY=replace-with-a-random-secret-at-least-32-characters-long
```

Replace the database connection values with your PostgreSQL credentials and use a private, random secret for `JWT_SECRET_KEY`.

In PowerShell:

```powershell
cd .\backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. The tables are created when the API starts; the database itself must already exist.

### 3. Start the frontend

Open a second terminal from the `Day18` directory:

```powershell
cd .\frontend
npm ci
npm run dev
```

Open the local URL printed by Vite (normally `http://localhost:5173`). The frontend uses `http://localhost:8000` as its default API URL. To change it, copy `.env.example` to `.env.local`, update `VITE_API_URL`, then restart the Vite server.

### API explorer

With the backend running, open [Swagger UI](http://localhost:8000/docs) or [ReDoc](http://localhost:8000/redoc).

## API documentation

**Local base URL:** `http://localhost:8000`

All endpoints below require `Authorization: Bearer <access_token>` except registration, login, and the health check. The access token is valid for 30 minutes. Use the **Authorize** control in Swagger UI to try protected endpoints.

### Authentication and health

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `POST` | `/auth/register` | Public | Create an account; returns `201 Created`. |
| `POST` | `/auth/login` | Public | Sign in and receive an access token. |
| `GET` | `/auth/me` | User | Return the signed-in user's ID, email, and role. |
| `GET` | `/health` | Public | Return `{"status":"ok"}` when the API is running. |

Registration and login accept a JSON body with `email` and `password`. Email is normalized to lowercase; passwords must be 8–128 characters. Registering an existing email returns `409 Conflict`. A successful login returns `access_token`, `token_type` (`bearer`), and `expires_in` (seconds).

### Movies and genres

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/movies` | User | List the signed-in user's movies. |
| `GET` | `/movies/{movie_id}` | User | Get one of the signed-in user's movies. |
| `POST` | `/movies` | User | Add a movie; returns `201 Created`. |
| `PUT` | `/movies/{movie_id}` | User | Replace a movie's editable fields. |
| `PATCH` | `/movies/{movie_id}/watched` | User | Set the watched status. |
| `DELETE` | `/movies/{movie_id}` | User | Delete a movie; returns `204 No Content`. |
| `GET` | `/genres` | User | List distinct genres in the signed-in user's library. |

`GET /movies` supports optional `search` and `genre` query parameters. Search matches part of a title; genre matches a genre without case sensitivity. Both parameters default to an empty string.

The `POST` and `PUT` request body uses these fields:

```json
{
  "title": "Inception",
  "genre": "Sci-Fi",
  "release_year": 2010,
  "rating": 8.8,
  "watched": true,
  "poster_url": "https://example.com/inception.jpg"
}
```

`title` (1–120 characters), `genre` (1–40 characters), `release_year` (1888–2100), and `rating` (0–10) are validated. `watched` defaults to `false`; `poster_url` is optional and must be an HTTP or HTTPS URL when provided. A watched-status update accepts `{"watched": true}` or `{"watched": false}`.

Movie responses also include `id` and `owner_id`. Users can only read or modify their own movies; inaccessible or missing movie IDs return `404 Not Found`.

### Administrator endpoints

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/admin/users` | Admin | List user IDs, emails, and roles. |
| `GET` | `/admin/movies` | Admin | List all movies, including owner details. |

These endpoints require a valid token belonging to an administrator account. A non-admin account receives `403 Forbidden`.

### Common responses

- `200 OK`: successful read, update, or login.
- `201 Created`: successful registration or movie creation.
- `204 No Content`: successful movie deletion.
- `401 Unauthorized`: missing, invalid, or expired bearer token; or invalid login credentials.
- `403 Forbidden`: the account does not have administrator access.
- `404 Not Found`: the requested movie is not in the signed-in user's library.
- `409 Conflict`: an account already exists for the submitted email.
- `422 Unprocessable Entity`: request fields failed validation.

## Future improvements

- Add automated API tests for authentication, authorization, validation, and movie CRUD.
- Introduce database migrations so schema changes can be applied safely to existing installations.
- Add pagination and server-side sorting for larger movie collections.
- Add richer filters, such as watched status, release-year range, and rating.
- Add password reset and email verification flows.
- Expand responsive and accessibility testing across screen sizes and assistive technologies.
- Improve deployment configuration and environment-specific CORS settings.
- Explore integration with a movie metadata service to look up posters and film details.

## Contributing

Contributions and suggestions are welcome. For a change, create a focused branch, make and test the update, and open a pull request describing what changed.

## Author

[Puneet Goswami](https://github.com/puneetg0)
