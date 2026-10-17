# Day 21 - Getting CineShelf Ready for a Release

**Internship:** Python Full Stack Developer Internship
**Project:** CineShelf movie library
**Day 21 focus:** Check the application like a release engineer: test the API, check authentication and validation, make deployment instructions repeatable, and explain the system clearly.

> This is a learning and release-preparation milestone, not a claim that the application has already been deployed and proven in production. The app code is in `Day18/`; Day 21 adds API tests, deployment files, DSA practice, and this guide.

## What I did today

- Added automated tests for registration, login, protected endpoints, movie validation, movie create/edit/delete, ownership, and administrator-only endpoints.
- Tested that a broken password record cannot ask the server to run an unlimited amount of password-hashing work.
- Made the allowed frontend website addresses configurable for deployment.
- Changed the health check so it also tries a small database query. If the database is unreachable, the service should not report itself as healthy.
- Added Docker build instructions for the FastAPI API and React website, plus a Compose file that connects them.
- Added two Python practice problems and tests for them.
- Wrote down the current limitations so a passing local test is not confused with a completed production launch.

## How to explain CineShelf in everyday language

### What does the app do?

“CineShelf is a website for keeping a personal list of movies. A person can make an account, sign in, add movies, search or filter their list, and mark movies as watched. An administrator has a separate view for looking at users and movies.”

### How does sign-in work?

“When someone creates an account, the server does not save their password as readable text. It saves a protected version of the password. When the person signs in, the server checks the password and gives the website a short-lived access token. The website sends that token with later requests to prove who the person is. The server checks the token and looks up the account before it returns private information. The token is kept in memory by the website, so the person signs in again after a full page reload.”

The password is hashed using PBKDF2-SHA256. The access token is signed using HS256 and expires after 30 minutes. The API checks the user's current role from the database; the browser's selected role does not grant administrator access.

### What is in the database?

“There are user records and movie records. A user has an email, a protected password hash, and a role. A movie has a title, genre, year, rating, watched status, and optional poster URL. Each movie also has an owner ID. That owner ID is how the API knows which movies belong to which account.”

The movie owner ID refers to the user's database ID. The database model allows older movie rows to have no owner. The registration code assigns eligible legacy movie rows to the first account, so this behavior should be considered carefully before migrating an existing production database.

### How is the website split into parts?

“The React app has an app-level part for signing in and deciding which screen to show. The movie-library feature handles the personal library. A reusable movie-card component displays one movie, and shared style files control how the screens look. The FastAPI backend is split into routes, database models, and validation schemas so each part has a clear job.”

- `Day18/frontend/src/App.jsx` handles sign-in, account checks, and the administrator screen.
- `Day18/frontend/src/features/library/MovieLibrary.jsx` handles the movie collection and movie actions.
- `Day18/frontend/src/components/MovieCard.jsx` displays a movie card.
- `Day18/backend/app/routes/` contains the API endpoints.
- `Day18/backend/app/schemas/` checks incoming movie data and shapes API responses.
- `Day18/backend/app/models/` describes the movie table.

### How does the website talk to the server?

“The browser sends HTTP requests to the FastAPI server. It sends and receives JSON. For private requests, it also sends the access token in the `Authorization` header. The server checks the request, reads or changes the database, and sends back a response. If the information is invalid, the API returns a validation error instead of saving it.”

The API address is `VITE_API_URL` in the frontend. Vite puts this value into the frontend when it builds the website, so it must be set to the public API address before building a production frontend.

## Project layout

```text
Day18/
  backend/
    app/
      auth.py                 # Accounts, password hashing, tokens, access checks
      database.py             # Database engine and request-scoped sessions
      main.py                 # FastAPI app, CORS, health endpoint, routers
      models/                 # Database table definitions
      routes/                 # Movie and administrator API endpoints
      schemas/                # Request validation and response formats
    Dockerfile
    requirements.txt
    requirements-dev.txt
    .env.example
  frontend/
    src/
      App.jsx                 # Sign-in and administrator screens
      components/             # Reusable UI pieces
      features/library/       # Movie-library behavior and screens
      styles/                 # Shared, sign-in, and library styles
    Dockerfile
    nginx.conf
    package.json
  tests/
    test_api.py               # FastAPI API regression tests
    test_practice.py          # Earlier DSA practice tests
Day21/
  docker-compose.yml          # Runs the Day18 frontend and backend containers
  dsapractice.py              # Day 21 DSA solutions
  test_day21.py               # Day 21 DSA tests
  README.md                   # This guide
```

## Running the application locally

### You will need

- Python 3.12 (the backend container uses Python 3.12).
- Node.js 22 and npm.
- A PostgreSQL database that CineShelf can connect to.

### 1. Set up the backend

Open PowerShell in the repository folder and run:

```powershell
cd Day18\backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
```

Edit `Day18/backend/.env` and replace the example database address and secret. Do not commit `.env`. Make a long, random `JWT_SECRET_KEY` for your own environment; do not copy the example value into a real deployment.

Start the API:

```powershell
python -m uvicorn app.main:app --reload
```

The API documentation is at <http://localhost:8000/docs>. The health check is at <http://localhost:8000/health>.

### 2. Set up the frontend

In a second PowerShell window:

```powershell
cd Day18\frontend
npm ci
npm run dev
```

Open <http://localhost:5173>. The checked-in `Day18/frontend/.env.example` points the local website at `http://localhost:8000`.

## API reference

Open `/docs` while the backend is running to try these endpoints interactively. Except for registration, login, and health, requests need an access token in the `Authorization: Bearer <token>` header.

The endpoint-by-endpoint request and response reference is also available in [`Day18/docs/API.md`](../Day18/docs/API.md).

| Method | Path | Who can use it | What it does |
|---|---|---|---|
| `GET` | `/health` | Anyone | Checks that the API can run a simple database query. |
| `POST` | `/auth/register` | Anyone | Creates a regular user account. Email is trimmed and made lowercase. |
| `POST` | `/auth/login` | Anyone | Checks email and password and returns a short-lived access token. |
| `GET` | `/auth/me` | Signed-in user | Returns the signed-in user's ID, email, and role. |
| `GET` | `/movies` | Signed-in user | Lists that user's movies. Optional `search` and `genre` filters are available. |
| `GET` | `/movies/{movie_id}` | Signed-in user | Gets one of that user's movies. Other users' movies appear as not found. |
| `POST` | `/movies` | Signed-in user | Adds a movie to that user's library. |
| `PUT` | `/movies/{movie_id}` | Movie owner | Replaces the editable details of that movie. |
| `PATCH` | `/movies/{movie_id}/watched` | Movie owner | Changes whether that movie has been watched. |
| `DELETE` | `/movies/{movie_id}` | Movie owner | Deletes that movie. |
| `GET` | `/genres` | Signed-in user | Lists the genres in that user's library. |
| `GET` | `/admin/users` | Administrator | Lists account IDs, emails, and roles. |
| `GET` | `/admin/movies` | Administrator | Lists movies across accounts, including each owner's email. |

Example movie request:

```json
{
  "title": "Arrival",
  "genre": "Science Fiction",
  "release_year": 2016,
  "rating": 8.0,
  "watched": false,
  "poster_url": null
}
```

The API checks that the title and genre are not blank, the year is between 1888 and 2100, the rating is between 0 and 10, and a poster URL (if supplied) uses HTTP or HTTPS. The browser also checks form values to help the person fix mistakes before sending the request. Server-side checks still apply even if a browser check is bypassed.

## Tests and quality checks

From the repository folder, after installing `Day18/backend/requirements-dev.txt`:

```powershell
python -m pytest Day18\tests Day21\test_day21.py
```

The API tests use a temporary SQLite database, not the configured PostgreSQL database. They cover account registration, login, invalid credentials, missing or invalid tokens, movie validation and CRUD, ownership isolation, administrator permissions, unhealthy password-hash values, token expiry, and the health endpoint.

Check the frontend separately:

```powershell
cd Day18\frontend
npm run lint
npm run build
```

These checks confirm that code passes tests, linting, and compilation. They do not by themselves prove that the app works on every phone, that a real hosted database is configured correctly, or that a public deployment is secure.

## Docker run-through

The Compose setup runs the Day18 FastAPI and React containers. It expects a PostgreSQL database to exist already; it does not create or host a database for you.

1. Copy `Day21/.env.example` to `Day21/.env`.
2. Edit `Day21/.env` with a reachable PostgreSQL URL, a new random secret, the frontend's browser origin in `CORS_ORIGINS`, and the public API URL in `VITE_API_URL`.
3. From the repository folder, run:

```powershell
docker compose --env-file Day21/.env -f Day21/docker-compose.yml up --build
```

4. Open <http://localhost:3000>. Check <http://localhost:8000/health> and <http://localhost:8000/docs>.
5. Stop the containers with:

```powershell
docker compose --env-file Day21/.env -f Day21/docker-compose.yml down
```

The Compose file waits for the API health check before starting the frontend. In a real deployment, use HTTPS, set the actual frontend origin and API address, protect environment variables in the hosting platform, and use a managed database with backups.

## Bug report and changes made

| Finding | Why it mattered | Change |
|---|---|---|
| A saved password hash could claim an extremely large number of PBKDF2 rounds. | A login attempt could consume excessive CPU if a damaged or manipulated hash reached the database. | The verifier now accepts only the current supported range (600,000 to 1,000,000 rounds); a regression test checks an excessive value. |
| The API health check always replied `ok`, even if its database was unavailable. | A deployment monitor could mistake an API with a broken database connection for a healthy service. | `/health` now executes `SELECT 1` using the request database session. |
| CORS only allowed the two local Vite development addresses. | A deployed browser frontend on a different domain could be blocked from calling the API. | The API reads a comma-separated `CORS_ORIGINS` allowlist from the environment and rejects an empty list. |
| There were no automated API tests in the Day18 test folder. | Sign-in, ownership, permissions, and validation changes could break without being noticed. | Added `Day18/tests/test_api.py` with endpoint regression cases using a temporary database. |

The same findings are listed as a short bug report in [`BUG_REPORT.md`](./BUG_REPORT.md).

## Things still required before a real production launch

- **Database migrations:** the app currently creates its tables during startup. A real release should use a migration tool and reviewed migration scripts before changing a live database.
- **Admin account setup:** registration intentionally creates a regular user. Define a secure, documented administrator bootstrap process; do not make public registration accept an `admin` role.
- **Deployment settings:** set real HTTPS URLs, CORS origins, database credentials, secret values, backups, and hosting health checks in the deployment platform. Never put actual secrets in Git.
- **Abuse protection:** add and test login rate limiting and any account recovery policy before exposing sign-in publicly.
- **Release verification:** run the test/build commands, deploy to a staging environment, and test the actual domain, database, authentication, and mobile layout before release.
- **Visual check:** the sign-in screen, signed-in movie library (including the add-movie dialog), and administrator dashboard were checked in a browser at 320, 375, 768, and 1280 CSS-pixel widths. No horizontal overflow remained after the fix. This is a useful layout check, not a substitute for broader accessibility or device testing.
- **Responsive fix:** the authenticated library navigation originally overflowed on narrow phones. The header now places the brand and account buttons on one row and the navigation on a second row.

Therefore, this milestone improves release readiness and creates a repeatable local container setup. It does **not** claim that a public production deployment has been completed or audited.

## DSA practice

### 1. Longest Substring Without Repeating Characters

**In plain language:** Find the longest stretch of letters in a string where no letter appears twice. The letters must stay next to each other; we cannot skip letters.

Examples:

| Input | Answer | Why |
|---|---:|---|
| `"abcabcbb"` | `3` | `"abc"` has no repeated letters; a longer stretch repeats one. |
| `"bbbbb"` | `1` | Every next character is another `b`. |
| `"pwwkew"` | `3` | `"wke"` is a valid stretch of length three. |

**How the code works:** Keep track of the start of the current valid stretch. Remember the last position where each character appeared. When a repeated character is inside the current stretch, move the start just past its previous position. Keep the largest stretch length seen so far.

**How to explain the speed:** “I look at each character once and use a dictionary to jump past repeats, so the running time is O(n). The dictionary can hold up to one entry per different character, so the extra space is O(n).”

### 2. Merge Intervals

**In plain language:** Each pair is a start and end point, like a booking from day 1 to day 3. If two bookings overlap, combine them into one longer booking.

Example:

```text
Input:  [(1, 3), (2, 6), (8, 10), (9, 12)]
Output: [(1, 6), (8, 12)]
```

**How the code works:** Sort the intervals by their start. Look at them from left to right. If the next interval starts before the current one ends, extend the current end if needed. If it starts later, finish the current interval and start a new one.

**How to explain the speed:** “Sorting takes O(n log n). After sorting, I check each interval once, which takes O(n). The sorted list and output use O(n) extra space.”

Try the solutions in `Day21/dsapractice.py`. Their tests include repeated letters, empty input, nested intervals, and intervals that touch at an endpoint.

## Short presentation you can say out loud

> “For Day 21, I prepared CineShelf for a release review. I added tests for the important API behavior: accounts, sign-in, validation, movie operations, and making sure one user cannot read another user's movies. I also improved the health check so it checks the database, made the frontend's allowed origin configurable, and added Docker instructions. The app stores users and movies in a database, and each movie belongs to an owner. The React frontend sends JSON requests to FastAPI and includes a short-lived token for private requests. I still need database migrations, a secure admin setup, and a real staging deployment before calling it production-ready.”
