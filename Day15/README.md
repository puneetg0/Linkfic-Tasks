# CineShelf — Day 15: Roles and Admin Dashboard

Day 15 continues the CineShelf project from Day 13–14. It keeps the existing
registration, login, logout, JWT session, protected personal movie library, and
PostgreSQL data. This update adds basic `user` and `admin` roles:

- A **user** can see and manage only movies in their own library.
- An **admin** can view all registered users and every movie, including the
  email address of the movie's owner. The admin view is read-only.
- The sign-in form lets the person choose **User** or **Admin**. This selection
  only chooses the expected account role; the API still checks the account's
  actual stored role and never grants privileges based on the selection.
- FastAPI checks the role on each admin API request. Hiding the admin screen in
  React is not treated as security.

The Day 15 frontend is in this folder. It reuses the Day 13–14 login flow and
the Day 11 CineShelf dashboard instead of making copies. The FastAPI backend
and PostgreSQL database remain in `../Day11/backend`.

## What changed today

1. Added a `role` field to CineShelf accounts. New accounts are always
   registered as `user`; the public registration form cannot choose a role.
2. Added a database migration that keeps existing accounts as regular users
   until a trusted operator promotes an account.
3. Added `GET /admin/users` and `GET /admin/movies`. Both require a valid JWT
   belonging to an admin. The movie list includes its owner's email.
4. Added a read-only admin dashboard with tabs for all users and all movies.
5. Added an explicit backend command to promote or demote an existing account.
6. Kept ordinary movie and genre endpoints restricted to the signed-in user's
   own collection.
7. Added Two Sum and Longest Common Prefix practice examples in
   `practice_day15.py`.

## Topics in simple words

| Topic | Brief explanation | Where CineShelf uses it |
| --- | --- | --- |
| Authentication | Confirms which account is signing in. | Email/password login and the API's current-user dependency. |
| Authorization | Checks what an authenticated account may do. | The user role can access its own library; the admin role can read global listings. |
| Password hashing | Stores a one-way password verifier rather than the original password. | Existing PBKDF2-HMAC-SHA256 hash and constant-time password comparison. |
| JWT | A signed token containing identity and expiry information. Its contents are not encrypted. | The frontend sends the short-lived token in the `Authorization: Bearer` header. |
| Protected route | A frontend navigation boundary for a signed-in view. | Opening `#/dashboard` without an in-memory token returns to sign-in. |
| Protected API | A backend boundary that checks credentials before returning private data. | Movie routes require a valid user; admin routes additionally require role `admin`. |
| Role-based access | Access is granted based on an account's assigned role. | `user` and `admin` are stored in the account table; registration cannot self-assign admin. |
| Session vs token | A server session stores session state server-side; a bearer token is sent with requests and verified by the API. | This learning app uses an expiring JWT held in frontend memory. A refresh signs out. |
| Unauthorized response | `401` means missing or invalid authentication; `403` means authenticated but not allowed. | Invalid/missing tokens get 401; a regular user calling `/admin/...` gets 403. |

## How access works

```text
User:
  login -> JWT -> own movies/genres -> create, edit, watch, delete own movies

Admin:
  login -> JWT -> /auth/me returns role=admin
                   -> /admin/users lists account id, email, role
                   -> /admin/movies lists each movie and its owner

No token -> 401 Unauthorized
Valid user token on an admin API -> 403 Forbidden
```

The admin listing APIs are read-only. Admin access does not bypass the normal
ownership rules for movie edits or deletes. Movie writes continue to be
scoped to the authenticated owner's `owner_id`.

## Run the project (PowerShell)

### 1. Configure the backend and migrate the database

PostgreSQL must be running, and `Day11/backend/.env` must contain a private
`DATABASE_URL` for the CineShelf database. Do not add `.env`, database
credentials, passwords, or JWT secrets to GitHub.

Open PowerShell:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day11'

$bytes = New-Object byte[] 48
$rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
$rng.GetBytes($bytes)
$env:JWT_SECRET_KEY = [Convert]::ToBase64String($bytes)

.\backend\.venv\Scripts\python.exe -m backend.migrate_day15
.\backend\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload --port 8000
```

Keep this terminal open. The Day 15 migration also runs the Day 14 ownership
migration, then adds a non-null `role` column with default `user` if it is not
already present. It is safe to run again. Existing movies keep their current
owners; legacy unassigned movies follow the Day 14 migration rule.

If the project uses a different Python virtual environment, activate that
environment and install `Day11/backend/requirements.txt` before running these
commands. The API documentation is available at
`http://localhost:8000/docs`.

### 2. Start the Day 15 frontend

Open a second PowerShell terminal:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day15'
npm install
npm run dev
```

Open the local Vite URL printed in the terminal, usually
`http://localhost:5173`. The frontend uses `http://localhost:8000` by default.
To select a different API address, create a local `Day15/.env` file:

```text
VITE_API_URL=http://localhost:8000
```

Restart Vite after changing the API URL.

### 3. Create an admin account

Register a normal account in CineShelf first. In a separate PowerShell
terminal, run the following trusted backend command, replacing the email with
the account to promote:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day11'
.\backend\.venv\Scripts\python.exe -m backend.set_user_role admin@example.com admin
```

Sign out and sign back in for the role to appear in the UI. The command can
also demote an admin:

```powershell
.\backend\.venv\Scripts\python.exe -m backend.set_user_role admin@example.com user
```

Only someone with trusted access to the backend/database should run this
command. Never add a role selector to public registration: a user must not be
able to promote their own account. Admin promotion/demotion takes effect on the
next API request because the backend loads the current role from the database.

## Try the features

1. Register or sign in as a regular user. Add a movie and verify that the
   dashboard shows its personal library.
2. Sign in as a second regular user. Its library is separate; it cannot access
   the first user's movie through movie APIs.
3. Promote a test account with `backend.set_user_role` and sign in again.
4. Use the sign-in **User/Admin** selector that matches the account's assigned
   role. Choosing Admin does not promote a regular user; a mismatched choice
   shows an error instead of opening the admin dashboard.
5. Switch between **All movies** and **All users** in the admin dashboard.
   Movie rows show the owning email, including `Unassigned` where a legacy
   record has no account owner.
6. Sign out. The in-memory token is removed, the dashboard is protected, and
   an attempt to use an API without a valid token receives `401`.
7. With a normal user token, call `/admin/users` or `/admin/movies` in
   `/docs`; the API returns `403 Forbidden`.

## API endpoints

| Endpoint | Access | Purpose |
| --- | --- | --- |
| `POST /auth/register` | Public | Create a regular user account. |
| `POST /auth/login` | Public | Verify credentials and issue an expiring JWT. |
| `GET /auth/me` | Authenticated | Return the signed-in account id, email, and role. |
| `GET /movies`, `GET /movies/{id}`, `GET /genres` | Authenticated | Read the current user's collection and genres. |
| `POST /movies`, `PUT /movies/{id}`, `PATCH /movies/{id}/watched`, `DELETE /movies/{id}` | Authenticated owner | Manage only movies owned by the current user. |
| `GET /admin/users` | Admin only | List user id, email, and role; never password hashes. |
| `GET /admin/movies` | Admin only | List movies from all libraries with owner email. |

## Day 15 coding practice

Run the examples and their assertions:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day15'
..\Day11\backend\.venv\Scripts\python.exe .\practice_day15.py
```

- **Two Sum:** scan the numbers once and store each previously seen number's
  index in a dictionary. For each number, look up its complement. Average
  lookup is constant time, so the algorithm takes `O(n)` time and `O(n)` space.
- **Longest Common Prefix:** shrink the candidate prefix until each word
  starts with it. The example words `flower`, `flow`, and `flight` produce
  `fl`.
- **Password hashing basics:** passwords are not encrypted for later recovery.
  CineShelf hashes a password with a random salt, then checks a login attempt
  using a constant-time digest comparison. Do not print real passwords or
  stored hashes in a demo.
- **Protected routes:** React can guide navigation, but an attacker can call an
  API directly. FastAPI must verify both the token and the required role.

## Validate changes

From `Day15`:

```powershell
npm run lint
npm run build
```

From `Day11`:

```powershell
.\backend\.venv\Scripts\python.exe -m compileall backend
```

## Project layout

```text
Day15/
  src/
    App.jsx             Day 15 entry that reuses the Day 13–14 auth application
    App.css             Reuses the auth theme and admin dashboard styles
    main.jsx            React entry point
  practice_day15.py     Two Sum and Longest Common Prefix
  README.md             Day 15 topics, setup, demo, and learning notes
  package.json          Day 15 Vite scripts and dependencies
  vite.config.js        Shares React and the existing CineShelf dashboard

../Day1314/src/
  App.jsx               Login, protected dashboard, and role-selected admin view
  App.css               Login styles and the Day 15 administrator dashboard

../Day11/backend/
  auth_day13.py         Authentication, current-user and admin dependencies
  routes/admin.py       Admin-only all-users and all-movies endpoints
  routes/movie.py       Protected, per-owner personal movie endpoints
  migrate_day15.py      Day 15 database role migration
  set_user_role.py      Trusted command to promote/demote an account
```
## Concepts + DSA Practice
CineShelf movie collection project. For the DSA problems, we'll use simple Python for loops and if conditions so you can understand the logic before learning advanced techniques.


**1. Authentication vs. Authorization**
These two terms sound similar, but they have different purposes.
Authentication — Who are you?
Authentication checks whether you are the person you claim to be.
Example: You enter your email and password to log in to CineShelf.
Question: Are you logged in as a valid user?


Authorization — What are you allowed to do?
Authorization checks what actions you are permitted to perform.
Example: A regular user can edit their own movies, but only an admin can access the admin dashboard.
Question: Do you have permission to perform this action?


Remember it like this:
- Authentication = identity.
- Authorization = permission.

- 
**2. Why is JWT widely used?**
JWT stands for JSON Web Token. It is a compact token that can carry information about a user's identity and other claims.
For example, after a successful login, your FastAPI backend can issue a JWT. React can send that token with later API requests.
The process looks like this:
1. User logs in
Email + password

2. FastAPI verifies credentials
Returns a signed JWT if valid

3. React sends the token
With protected API requests

4. FastAPI verifies the token
Checks identity and permissions


Why developers use JWT:
- It lets the backend verify signed claims without looking up a server-side session for every request.
- It works well with React frontends and FastAPI APIs.
- It can include an expiration time.
- It can carry claims such as a user ID and role.
Important: JWT payloads are generally readable, not secret. Never put passwords in them. A signed JWT is also not automatically encrypted or revocable.

**3. Protected Routes**
A protected route is a page that requires the user to meet certain conditions before accessing it.
Examples in CineShelf:
Route	Who can access it?
/login	Everyone
/movies	Logged-in users
/admin	Logged-in admins only
If a logged-out user tries to open /movies, React can redirect them to /login.
However, frontend protection alone is not security. FastAPI must also verify the token and permissions before returning private data or performing an action.

**4. API Security**
API security means protecting your backend endpoints from unauthorized access and misuse.
Suppose CineShelf has this endpoint:
DELETE /movies/10
Before deleting movie 10, your backend should check:
1. Is the request authenticated with a valid token?
2. Does movie 10 exist?
3. Does the movie belong to the current user, or does the user have an explicitly authorized admin permission?
4. Is the requested action allowed?
If another user owns that movie, the request must not delete it.
Other important security practices include password hashing, input validation, HTTPS, appropriate CORS settings, and avoiding the exposure of private user data.

**5. Session vs. Token Authentication**
Session authentication	Token authentication
Server stores session information.	Client sends a token with requests.
Browser commonly sends a session cookie.	Often uses a bearer token or a cookie.
Server can invalidate a session centrally.	Revoking a self-contained JWT generally needs extra mechanisms.
Common in traditional web applications.	Common in APIs and distributed applications.
Both approaches can be secure when implemented properly. JWT is not automatically better than sessions.
For CineShelf, since you already use JWT, continue with your existing approach and focus on secure token verification and ownership checks.
Part 2: Python / Backend Practice

**6. Password Hashing Basics**
When a user creates a CineShelf account, you should never store their actual password directly in your database.
Instead, store a password hash.
For example:
- User enters password: movie123
- Backend hashes the password using a secure password-hashing algorithm.
- Database stores the hash instead of the original password.
- During login, the backend verifies the entered password against the stored hash.
A common beginner-friendly option is Argon2, or bcrypt. Here is an example using Argon2.
Install the library:
pip install "pwdlib[argon2]"


Example:
from pwdlib import PasswordHashpassword_hash = PasswordHash.recommended()# Signup: hash the passwordpassword = "movie123"hashed_password = password_hash.hash(password)print("Stored hash:", hashed_password)# Login: verify the passwordentered_password = "movie123"if password_hash.verify(entered_password, hashed_password):    print("Login successful")else:    print("Invalid password")



Understand the code:
- PasswordHash.recommended() creates a password hasher with recommended settings.
- .hash(password) creates a secure password hash.
- .verify() checks whether the entered password matches the stored hash.
You don't decrypt a password hash during login. You verify the password instead.
In your project, store hashed_password in the database, never the original password.
7. Dictionary Lookup Optimization
A Python dictionary stores information as key-value pairs.
Suppose you want to find a movie's rating using its ID.
movie_ratings = {    101: 8.5,    102: 7.9,    103: 9.0,    104: 8.2}movie_id = 103if movie_id in movie_ratings:    print(movie_ratings[movie_id])else:    print("Movie not found")



Output:
9.0


Why use a dictionary?
- Searching through a list may require checking many items one by one.
- A dictionary typically finds a key in O(1) average time.
- This can make lookups faster when you have many records.
For example, a dictionary can help find a movie by ID. In a real database-backed CineShelf application, you would generally query the database rather than load every movie into a Python dictionary.
Part 3: Frontend / React Practice
## 8. Protected Routes
A protected route prevents users from accessing certain pages unless they meet the required conditions.
For example, in CineShelf:
- /login — accessible to everyone.
- /movies — accessible to authenticated users.
- /admin — accessible only to admins.
React checks the user's authentication state and redirects them when necessary. FastAPI independently verifies authentication and authorization for each protected API request.
Why is authentication important?
Authentication helps your application identify users so it can protect private information, associate movie records with the correct accounts, and restrict actions to the appropriate people.
Without authentication, anyone might be able to access information that should be private.


## What I learned

- Authentication identifies the account; authorization decides which data
  that account can access.
- A valid JWT is not automatically an admin credential. The server loads the
  account's stored role and checks it for every admin request.
- A React protected route is useful for the experience, but only the backend
  can enforce data security.
- `401 Unauthorized` indicates missing or invalid authentication; `403
  Forbidden` indicates a valid account without the required permission.
- User-owned movie queries stay isolated, while admin reporting uses dedicated
  read-only routes. Account and movie visibility is not granted to ordinary
  users.
- A dictionary makes complement lookups efficient in Two Sum, and shortening
  a prefix provides a direct solution to Longest Common Prefix.

The project is for learning. The JWT is held only in frontend memory, so a
browser refresh signs the user out. A real deployment would also need a
production session strategy, HTTPS, secure secret management, stronger
operational controls, and a security review.
