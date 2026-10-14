# CineShelf - Day 18

Day 18 gives CineShelf a self-contained, cleaner project layout. The existing
movie library, registration and sign-in, role-based admin view, and FastAPI API
are kept together here instead of importing source files from earlier day
folders.

## What changed

- Grouped the React application by feature and moved the reusable `MovieCard`
  into `frontend/src/components`.
- Kept authentication, the movie library, and shared styles inside the
  standalone `frontend` app; removed the cross-day Vite alias.
- Grouped FastAPI modules under `backend/app`, with separate `routes`, `models`,
  and `schemas` packages.
- Renamed the day-specific `auth_day13.py` module to `auth.py` and updated the
  imports.
- Excluded generated files, local databases, virtual environments, and secrets
  from the deliverable. `backend/.env.example` documents the required settings.
- Added tested, reusable DSA functions for merging sorted arrays and finding
  repeated values.

## Project structure

```text
Day18/
├── backend/
│   ├── .env.example
│   ├── requirements.txt
│   └── app/
│       ├── auth.py
│       ├── database.py
│       ├── main.py
│       ├── models/
│       ├── routes/
│       └── schemas/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── features/library/
│   │   └── styles/
│   ├── package.json
│   └── vite.config.js
├── tests/
└── dsapractice.py
```

## Run CineShelf locally

### Backend

In PowerShell:

```powershell
cd Day18\backend
Copy-Item .env.example .env
```

Edit `.env` and set:

- `DATABASE_URL` to a reachable PostgreSQL database URL.
- `JWT_SECRET_KEY` to a unique random secret with at least 32 characters.

Then install and run the API:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`; interactive docs are at
`http://localhost:8000/docs`.

### Frontend

In a second PowerShell window:

```powershell
cd Day18\frontend
npm ci
npm run dev
```

The Vite dev server uses `http://localhost:5173`. If the API is hosted elsewhere,
create `frontend/.env.local` and set `VITE_API_URL` to the API base URL.

## Checks

```powershell
cd Day18\frontend
npm run lint
npm run build
cd ..\
python -m unittest discover -s tests -v
```

## DSA practice

`merge_sorted_arrays(first, second)` uses two pointers and copies the remaining
tail once one input is exhausted. It runs in **O(n + m)** time and uses
**O(n + m)** extra space.

`find_duplicates(numbers)` uses a set for membership checks and keeps each
repeated value once, in the order it first repeats. It runs in **O(n)** average
time and uses **O(n)** extra space.

The test suite covers empty inputs, duplicates, and equal values.

## Learn along the way

### Clean-code and React review

- Search YouTube for **“Clean Code principles for beginners”** and
  **“React component composition and reusability”**.
- Review component boundaries, meaningful names, one reason to change per
  module, and avoiding duplicated request and validation behavior.
- Recommended channels: **Web Dev Simplified**, **Codevolution**, and
  **Fireship**.

### FastAPI structure

- Search YouTube for **“FastAPI project structure routers schemas models”**.
- Trace a request through the router, schema, database dependency, and model.
- Compare API validation with the validation performed by the React form.

### Code review prompts

- Is a module in the right feature or layer?
- Does a name explain what the value or function represents?
- Can behavior be reused without hiding important intent?
- Do tests cover both typical input and important edge cases?
