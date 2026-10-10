# CineShelf — Day 13 + Day 14 Combined Project

This README explains what Day 13 and Day 14 asked us to build and learn, how
those ideas were added to CineShelf, how to run the project, and how to present
it from start to finish. It continues the Day 11–12 CineShelf project: this
folder provides the login and registration screen, while the original React
dashboard is reused from `../Day11/src/App.jsx`. The combined FastAPI API and
PostgreSQL database are in `../Day11/backend`.

## The combined Day 13 + Day 14 assignment

### Day 13: learn authentication and make a login page

The Day 13 task asked for a beginner login page and an introduction to
authentication:

- Learn what JWT authentication is and how login and registration work.
- Build a React login page and connect it to a FastAPI authentication API.
- Learn authentication versus authorization, JWT tokens, protected APIs, and
  secure applications.
- Practice hashing a password, comparing strings, explaining why routes need
  protection, longest common prefix, and valid anagram.

### Day 14: extend CineShelf into a full-stack application

The Day 14 client scenario asked us to enhance the Week 1 project rather than
start over:

- Add user registration and login.
- Connect a PostgreSQL database.
- Implement create, read, update, and delete (CRUD) operations.
- Keep the dashboard responsive and improve its UI and error messages.
- Add search and organize the project into clear frontend, backend, route,
  model, and schema responsibilities.
- Connect React, FastAPI, PostgreSQL, and authentication; update project
  documentation and prepare screenshots or a short demo.
- Learn to adapt to changing client requirements, reuse/refactor existing code,
  write clearer structures and documentation, and think about production
  improvements.
- Practice CRUD using classes, explaining React application flow, merging
  linked lists, and finding the best time to buy and sell stock.

### Beginner-friendly topic guide

| Topic | Simple explanation | Where it appears in CineShelf |
| --- | --- | --- |
| Authentication | Proving which account is signing in, usually with an email and password. | Registration and login forms call the FastAPI auth routes. |
| Authorization | Checking what the signed-in account is allowed to see or change. | Movie routes check each movie's owner before returning or changing it. |
| Password hashing | Turning a password into a one-way value for storage. The original password is not saved. | FastAPI hashes passwords during registration and verifies them during login. |
| JWT | A signed token that tells the API which account authenticated and when the token expires. It is signed, not encrypted. | FastAPI issues a token after login; React sends it with protected requests. |
| Protected route/API | A route that only works after the backend validates the user's token. | FastAPI protects movie and genre endpoints; React also shows login when signed out. |
| PostgreSQL + SQLAlchemy | PostgreSQL stores durable records; SQLAlchemy lets Python code work with those records as models and queries. | User and movie records are stored in the configured CineShelf database. |
| CRUD | Create, Read, Update, Delete—the common operations for managing records. | Add, list, edit, and delete movie actions. |
| Responsive UI | A layout that adjusts to different screen sizes. | The shared movie dashboard adapts its layout for desktop and smaller screens. |
| Error handling | Showing a useful failure message instead of pretending an operation worked. | Login, loading, movie save, and API failures are surfaced to the user. |

**Important distinction:** the frontend route guard improves navigation, but it
does not secure the data by itself. FastAPI must validate the JWT and enforce
ownership on every protected request.

## Presentation walkthrough

Use this order for a short live presentation. Start both servers using
[the setup steps](#run-the-project-powershell) before the audience arrives.
Have two test email accounts ready, but do not show or share real passwords,
database credentials, or the JWT secret.

### 1. Introduce the client request

**Show:** CineShelf and its login screen.

**Say:** “The original CineShelf could show and manage movies. The next
requirements were registration and login, a PostgreSQL-backed personal movie
collection, protected movie operations, search, and a responsive dashboard.
Rather than rebuilding the dashboard, I connected the existing Day 11–12
React app to the new authentication flow.”

This covers the changing client requirements, reuse/refactoring, React +
FastAPI integration, and the project structure.

### 2. Show registration and password handling

**Show:** Select **Create an account**, register the first demonstration
account, and show that it opens the dashboard. If appropriate, try registering
the same email again to show the duplicate-account error.

**Say:** “The browser sends the email and password to FastAPI. FastAPI validates
the input and stores a salted PBKDF2 password hash in PostgreSQL, never the
plain-text password. A password hash is one-way: at login we hash the submitted
password using the stored salt and compare the result securely.”

This covers login and registration, password hashing, string comparison, error
handling, and the difference between authentication and authorization:
authentication establishes who signed in; authorization checks what that
account is allowed to access.

### 3. Explain the JWT and protected API

**Show:** Open `http://localhost:8000/docs` if you want to show the FastAPI
routes. Then return to CineShelf and sign in.

**Say:** “After valid credentials, FastAPI returns a signed, expiring JWT.
React keeps it in memory and attaches it as a Bearer token to API requests.
FastAPI verifies the signature and expiration, looks up the account, and only
then runs a protected route. A React route guard improves the user experience,
but the API is the security boundary. Without a valid token, the API returns
401.”

The token is signed, not encrypted, and this learning project does not persist
it in browser storage. Refreshing the page signs the user out.

### 4. Demonstrate separate account libraries

**Show:** With the first registered account, browse the inherited Day 11–12
movies. Sign out, register or sign in with a second test account, and show that
it starts with its own empty collection. Add a movie to the second account and
then sign back into the first account to show the new movie is not visible
there.

**Say:** “Each movie row stores its owner's user ID. Every list, read, edit, and
delete operation is restricted to the signed-in account. The migration assigns
the pre-existing shared collection to the first registered account so legacy
movies are not left unowned; later accounts do not inherit that collection.”

**Important demo setup:** The current PostgreSQL database already has registered
accounts and its old movies assigned to the first account. Use the account that
owns the legacy collection to demonstrate those movies, and use another account
to demonstrate an isolated, empty library. Do not delete the existing sample
movies during the presentation.

This covers PostgreSQL integration, database migration, authentication,
authorization, and per-account data separation.

### 5. Demonstrate the dashboard and CRUD

**Show:** In the second account, add a movie, search for it, filter by genre,
toggle its watched status, edit it, and delete it. Confirm the delete prompt.

**Say:** “The existing responsive React dashboard provides the movie
collection, search, genre filter, and watchlist. FastAPI routes perform Create,
Read, Update, and Delete against PostgreSQL using SQLAlchemy. The movie model
is a Python class, and the route handlers enforce ownership before changing a
row. The dashboard has loading, empty, and error messages so failures are
visible instead of silently ignored.”

This covers CRUD, search, responsive UI, better UX, API/database structure, and
error handling. If presenting on a narrow screen, resize the browser to show
the responsive layout.

### 6. Prove access control and show useful errors

**Show:** Sign out and attempt to open `http://localhost:5173/#/dashboard`.
Then, optionally, use `/docs` to make a movie request without an authorization
token.

**Say:** “The login screen appears when there is no in-memory token, and
FastAPI independently rejects unauthenticated movie requests with 401.
Attempts to edit or delete a movie owned by another account return not found,
so the API does not reveal or allow changes to another user's movie.”

For one more visible error-handling example, try an incorrect password or a
duplicate registration and point out the message shown on the page.

### 7. Present the coding practice

Run the practice files before or during the presentation:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day1314'
& '..\Day11\backend\.venv\Scripts\python.exe' '.\dsapractice.py'
& '..\Day11\backend\.venv\Scripts\python.exe' '.\practice_day14.py'
```

Explain the examples briefly:

- **Longest Common Prefix:** compare characters across each word until one
  differs. The example words produce `fl`.
- **Valid Anagram:** compare whether two strings contain the same characters
  with the same counts. `listen` and `silent` are anagrams.
- **Merge Two Linked Lists:** repeatedly link the smaller current node; the
  example produces `1 -> 2 -> 3 -> 4 -> 5 -> 6`.
- **Best Time to Buy and Sell Stock:** keep the lowest earlier price and best
  profit seen so far; the example profit is `5`.
- **Password hashing and comparison:** `hash_password` creates a salted
  PBKDF2-HMAC-SHA256 hash, and `verify_password` safely checks a candidate
  password against that stored hash.

These are learning examples; do not display real passwords or a real stored
password hash in presentation screenshots.

### 8. Close with the implementation summary

**Say:** “The frontend is React, the API is FastAPI, and SQLAlchemy connects
the protected routes to PostgreSQL. JWT authentication identifies the
account; authorization scopes its movie collection. The original CineShelf
dashboard is reused, and the migration connects the previous movie records to
the new account model.”

If asked how the code is organized, point to:

- `Day1314/src/App.jsx`: login/register screen and authenticated dashboard
  wrapper.
- `Day1314/vite.config.js`: imports the original dashboard instead of copying
  it.
- `Day11/src/App.jsx`: CineShelf interface and movie actions.
- `Day11/backend/auth_day13.py`: account registration, login, password hashes,
  JWT creation, and token verification.
- `Day11/backend/routes/movie.py`: authenticated, owner-scoped movie API.
- `Day11/backend/models/db_models.py`: SQLAlchemy database models.
- `Day11/backend/migrate_day14.py`: migration and ownership assignment for
  older movies.

### Presentation checklist

- [ ] Start PostgreSQL and confirm `Day11/backend/.env` points to the intended
  database; keep `.env` private.
- [ ] Run the migration and start the FastAPI server.
- [ ] Start the React/Vite server and check the browser before presenting.
- [ ] Have two test accounts ready; know which one owns the original movies.
- [ ] Demonstrate registration/login, separate libraries, movie search, add,
  edit, watched status, delete, and sign out.
- [ ] Show at least one validation/authentication error and the protected API.
- [ ] Run both DSA practice scripts.
- [ ] Capture screenshots or a short recording of the login, dashboard, and
  per-account separation if a demo recording is required.
- [ ] Never show `.env`, passwords, JWT secrets, or database credentials.

## What is included

- Email registration and login with the Day 13 JWT authentication flow.
- Password hashes stored in the `day13_users` table (passwords are never stored
  as plain text).
- The existing responsive CineShelf dashboard, with its search, genre filter,
  watchlist, loading, and empty states.
- Protected movie API requests, add/edit/delete, and watched-status updates for
  movies owned by the signed-in account.
- Each account sees only its own movies. The first registered account receives
  the existing Day 11–12 collection; later accounts start with an empty library.

## Project layout

```text
Day1314/
  src/
    App.jsx             Login and protected wrapper around the shared dashboard
    App.css             Login page styles and Tailwind source configuration
    main.jsx            React application entry point
  practice_day14.py     Merge linked lists and stock-profit practice
  README.MD             This guide
  package.json          React and Vite scripts

../Day11/src/
  App.jsx               Original CineShelf dashboard and movie CRUD UI
  style.css             Existing movie dashboard styles
  index.css             Existing theme and Tailwind setup

../Day11/backend/
  main.py                Combined CineShelf API
  auth_day13.py          Registration, login, JWT creation and verification
  routes/movie.py        Protected movie CRUD and search routes
  models/db_models.py    SQLAlchemy movie and user database models
  migrate_day14.py       Safe, one-time movie ownership schema migration
```

## Run the project (PowerShell)

### 1. Prepare the database and backend

The backend reads `DATABASE_URL` from `Day11/backend/.env`. Keep that file and
your JWT secret private; never add credentials to GitHub.

Open a PowerShell terminal and run:

```powershell
cd "C:\Users\SPURG\Desktop\Linkfic Tasks\Day11"

$bytes = New-Object byte[] 48
$rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
$rng.GetBytes($bytes)
$env:JWT_SECRET_KEY = [Convert]::ToBase64String($bytes)

.\backend\.venv\Scripts\python.exe -m backend.migrate_day14
.\backend\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload --port 8000
```

Keep this terminal running. The migration creates the user table, adds an `owner_id` column to the existing
`movies` table if needed, and assigns old movies to the first registered
account. If no account exists yet, the first account created through the app
automatically receives those old movies. New movies belong only to the account
that created them. The migration checks the database before changing it, so it
is safe to run again.

If your backend virtual environment is not present, create/activate one and
install the packages from `backend/requirements.txt` before running the commands.
Make sure PostgreSQL is running and `DATABASE_URL` points at the CineShelf
database.

### 2. Start the React dashboard

Open a **second** PowerShell terminal:

```powershell
cd "C:\Users\SPURG\Desktop\Linkfic Tasks\Day1314"
npm install
npm run dev
```

Open the Vite URL printed in the terminal (usually `http://localhost:5173`).
The login and the reused dashboard both use the default API address
`http://localhost:8000`. To use a different API, create a local `.env` file in
`Day1314` with:

```text
VITE_API_URL=http://localhost:8000
```

Restart Vite after changing this setting.

### 3. Try the features

1. Choose **Create an account**, enter an email, and choose a password of at
   least eight characters.
2. Registration creates the account, hashes the password, and signs you in.
3. The dashboard requests your account and movie data using the JWT.
4. Search for a title, filter by genre or watched status, then add your own
   movie. Each account has a separate library, with edit, mark-watched, and
   delete controls for its own movies.
5. Sign out and try opening `#/dashboard`; without a token the login page is
   shown. The API also returns `401 Unauthorized` for movie requests without a
   valid token.

FastAPI's interactive API documentation is at `http://localhost:8000/docs`.

## How the React + FastAPI flow works

1. React posts credentials to `POST /auth/register` or `POST /auth/login`.
2. FastAPI validates input, stores only a salted password hash, and returns a
   signed, expiring JWT after a successful login.
3. React keeps the access token in memory and sends
   `Authorization: Bearer <token>` with dashboard API requests.
4. A FastAPI dependency verifies the token and finds its user before the
   protected movie route runs.
5. SQLAlchemy reads or changes PostgreSQL rows. Each movie stores the
   authenticated user's ID as its owner; reads, updates, and deletes are
   restricted to that account's movies.

The React route guard improves navigation but is not the security boundary:
FastAPI must also check every protected request. JWT payloads are signed, not
encrypted, so do not place secrets in them. This learning project keeps tokens
in memory (refreshing the browser signs you out) and is not yet a production
authentication setup.

## Day 14 coding practice

Run the two problem-solving examples with:

```powershell
cd "C:\Users\SPURG\Desktop\Linkfic Tasks\Day1314"
python practice_day14.py
```

`merge_sorted_lists` walks the two lists once and attaches the smaller next
node. `best_time_to_buy_and_sell` tracks the lowest earlier price and the best
profit so far in one pass.

## Validation

From this folder, run:

```powershell
npm run lint
npm run build
```

## What I learned

### Day 13: accounts, passwords, and tokens

- I learned that a login page is only the visible part of authentication. The
  backend must validate the credentials and decide whether they are correct.
- I learned not to store plain-text passwords. CineShelf stores a salted
  PBKDF2 password hash, then verifies a login attempt against that hash.
- I learned the difference between authentication (who is this account?) and
  authorization (which movies may this account access?).
- I learned that a JWT is a signed, expiring access token. The React app sends
  it to FastAPI, and FastAPI verifies it before allowing protected API
  operations.
- I learned that hiding a page in React is not enough to secure it. The backend
  must also reject missing or invalid tokens and check ownership.
- I practiced string comparison and the longest-common-prefix and valid
  anagram problems.

### Day 14: connecting a full-stack application

- I learned how the request moves through the application: React sends an HTTP
  request, FastAPI validates it and runs a route, SQLAlchemy queries or changes
  PostgreSQL, and FastAPI sends a response back to React.
- I learned how a database model represents stored data and how CRUD routes
  create, read, update, and delete movie records.
- I learned why ownership must be checked on the backend: each account should
  see and manage only its own movies.
- I learned how to extend an existing project by reusing its dashboard rather
  than making a second copy. The login flow and the original dashboard have
  separate responsibilities but work together.
- I learned to show loading, empty, and error states so users can tell what is
  happening when a request is delayed or fails.
- I practiced explaining a React application's flow, merging two sorted
  linked lists, and finding the best one-time stock profit.
- I learned that documentation and a repeatable demo are part of delivering a
  feature, not just writing code.

## What changed in CineShelf

Before this work, CineShelf already had a React movie dashboard and a FastAPI
backend connected to PostgreSQL. The Day 13 and Day 14 work extended those
parts:

1. **A sign-in and registration experience was added.** Users can create an
   account and sign in from the CineShelf-branded frontend.
2. **Authentication was added to FastAPI.** Passwords are stored as hashes,
   and successful login returns a signed, expiring JWT.
3. **Movie APIs became account-aware.** Movie and genre requests require a
   valid token; movie reads and changes are scoped to the authenticated owner.
4. **The PostgreSQL movie table gained ownership information.** The migration
   adds `owner_id` when needed and assigns older unowned movies to the first
   registered account. New movies are associated with the account that creates
   them.
5. **The original movie dashboard was connected, not copied.** The Day14
   frontend imports the dashboard from `Day11/src`, preserving its existing
   movie search, genre filter, watchlist, and responsive layout.
6. **Movie management is protected.** Accounts can add, edit, mark watched,
   and delete their own movies; another account cannot change those records.
7. **The guide and practice examples were expanded.** This README now explains
   the combined assignment, key topics in beginner-friendly language, setup,
   presentation flow, and learning outcomes.

The result is still a learning project, not a production-ready authentication
service. In particular, the access token is kept in memory and is lost when
the page is refreshed. Before a real production release, the application
would need additional security review, deployment configuration, monitoring,
and a production-appropriate session/token strategy.