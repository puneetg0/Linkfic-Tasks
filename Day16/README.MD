# CineShelf — Day 16: Validation and Error Handling

Day 16 improves CineShelf by validating form data in React and validating API
requests again in FastAPI. It also makes common failures easier to understand
and keeps the application stable when requests fail.

This folder contains a runnable Day 16 frontend. It reuses the authentication
and dashboard from Day 13–15 rather than copying the application. The shared
frontend and backend updates are in `../Day1314` and `../Day11`.

## Day 16 task checklist

| Task | CineShelf implementation |
| --- | --- |
| Add frontend form validation | Movie form checks required title and genre, text lengths, whole-number year, rating range, and optional poster URL. Errors appear beside the relevant inputs. |
| Add backend request validation | Pydantic validates movie fields and poster URLs; FastAPI constrains movie IDs and query lengths. |
| Handle API errors gracefully | Network failures, validation responses, unauthorized sessions, server errors, and unexpected response bodies are handled. |
| Display user-friendly messages | Form errors are actionable and field-specific where possible; other request failures use a clear message. |
| Validate required fields | Blank titles and genres are rejected after trimming whitespace. |
| Improve stability | Loading/submitting states prevent duplicate actions; the UI changes only after successful API responses, and failed edits retain the user's input. |
| DSA practice | `practice_day16.py` implements Valid Parentheses and Reverse Words in a String. |

## What changed in CineShelf

- **Controlled movie form:** React state stores the values as the user types.
- **Client-side checks:** the form checks the data before sending a request and
  identifies the field to fix.
- **Server-side checks:** the API repeats validation, even if someone skips
  the React interface and sends a request directly.
- **Safer poster URL:** poster links are optional, but when provided must use
  HTTP or HTTPS and fit within 2048 characters.
- **Readable API errors:** FastAPI validation details are converted to useful
  field messages; connection and server problems are reported separately.
- **Submission feedback:** save buttons show progress and are disabled during
  requests. Movies appear or update only after the API confirms success.
- **Practice examples:** includes required-text validation, targeted
  `ValueError` handling, Valid Parentheses, and Reverse Words.

## Frontend and backend validation

Frontend validation improves feedback but can be bypassed. Backend validation
is authoritative because every API client must pass through it. FastAPI
responds with `422 Unprocessable Entity` when request data is invalid.

| Movie field | Frontend validation | Backend validation |
| --- | --- | --- |
| Title | Required after trimming; maximum 120 characters. | Required, trimmed, 1–120 characters. |
| Genre | Required after trimming; maximum 40 characters. | Required, trimmed, 1–40 characters. |
| Release year | Required whole number from 1888 to 2100. | Integer constrained to 1888–2100. |
| Rating | Required number from 0 to 10. | Number constrained to 0–10. |
| Poster URL | Optional; HTTP/HTTPS only; maximum 2048 characters. | Optional; HTTP/HTTPS and length checked; blank becomes `null`. |

The frontend also keeps request errors visible and does not treat a failed
network call as a successful save.

## Concepts in simple words

### Why validation matters

Validation catches missing, incorrectly formatted, or out-of-range data before
it causes confusing behavior or gets stored. It also tells the user what to
correct instead of leaving them to guess.

### Controlled components

A controlled React input displays a value held in React state. The `onChange`
handler updates that state when the user types. In CineShelf, the movie form
uses that state both to display the current values and to validate the
submission.

```text
React state → input value → user types → onChange updates state
```

### Frontend vs backend checks

- **Frontend:** quick feedback and better form usability.
- **Backend:** enforces the rules for browsers, scripts, and any other API
  client; it is not optional even when the frontend already validates.

### Common application errors

- Missing or invalid form fields
- Wrong login credentials or an expired token
- A movie or account that cannot be found
- Network/API server unavailable
- An unexpected response from the server

### Better user feedback

Say what happened and what the user can do next. Keep their entered values
when a save fails. Show loading feedback while a request is in progress, and
only show the saved result after the server confirms it.

## Python input validation and exception handling

Validate input at the point where it enters a function. Strip whitespace from
required text, check type and allowed ranges, and raise a specific exception
for invalid input. Handle expected failures with targeted `except` clauses,
not a broad catch that hides unrelated bugs.

```python
def validate_required_text(value: str, field_name: str) -> str:
    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is required.")
    return cleaned_value


try:
    title = validate_required_text("   ", "Title")
except ValueError as error:
    print(error)
```

Output:

```text
Title is required.
```

The full runnable examples and assertions are in `practice_day16.py`.

## Day 16 DSA practice

### Valid Parentheses

Use a stack for opening brackets. When a closing bracket appears, it must match
the most recent opening bracket. The expression is valid when no mismatch
occurs and the stack is empty at the end. The implementation runs in `O(n)`
time and uses `O(n)` extra space.

Examples:

| Input | Result |
| --- | --- |
| `()[]{}` | Valid |
| `{[()]}` | Valid |
| `(]` | Invalid |
| `(((` | Invalid |

### Reverse Words in a String

Split the input on whitespace, reverse the words, and join them using one
space. This handles repeated and leading/trailing spaces as well.

```text
"  keep   spaces tidy  " → "tidy spaces keep"
```

The implementation takes `O(n)` time and space.

## Run the project (PowerShell)

### 1. Start the backend

Start PostgreSQL and ensure `Day11/backend/.env` has the correct
`DATABASE_URL`. Keep `.env`, database credentials, and JWT secrets private.

Open a PowerShell terminal:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day11'

$bytes = New-Object byte[] 48
$rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
$rng.GetBytes($bytes)
$env:JWT_SECRET_KEY = [Convert]::ToBase64String($bytes)

.\backend\.venv\Scripts\python.exe -m backend.migrate_day15
.\backend\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload --port 8000
```

Leave this terminal running. FastAPI's interactive documentation is at
`http://localhost:8000/docs`.

### 2. Start the Day 16 frontend

Open a second PowerShell terminal:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day16'
npm install
npm run dev
```

Open the URL printed by Vite, usually `http://localhost:5173`. By default,
the frontend connects to `http://localhost:8000`. To use another API URL,
create a local `Day16/.env` file with:

```text
VITE_API_URL=http://localhost:8000
```

Restart Vite after changing the API URL.

### 3. Run the Day 16 practice script

Open a third terminal:

```powershell
Set-Location 'C:\Users\SPURG\Desktop\Linkfic Tasks\Day16'
..\Day11\backend\.venv\Scripts\python.exe .\practice_day16.py
```

The script runs assertions and prints a success message if all checks pass.

## Presentation walkthrough

Use a test account and sample movie data. Start both servers before presenting.

1. **Introduce the goal:** Day 16 improves form feedback, rejects invalid API
   data, and explains failures instead of leaving users uncertain.
2. **Show controlled inputs:** sign in, open **Add movie**, and explain that
   React state holds the current form values and `onChange` updates them.
3. **Show frontend validation:** submit the blank form. Point out the inline
   title/genre/year/rating messages. Try an invalid year, rating, or poster
   URL, then correct the fields and save a valid movie.
4. **Show backend validation:** open `http://localhost:8000/docs`, expand
   `POST /movies`, click **Try it out**, and send an invalid payload such as a
   blank title or a rating of `12`. Point out the `422` response. Explain that
   direct API clients can bypass browser validation.
5. **Show friendly API failure handling:** with a test session, stop the
   development backend and try refreshing or saving. CineShelf should show a
   connection message and retain entered form data. Restart the backend
   before continuing. If you do not want to stop it, use an invalid login to
   show an API error message instead.
6. **Show stability:** point out the saving label and disabled button. Explain
   that the collection updates only after a successful API response.
7. **Run the DSA examples:** execute `practice_day16.py`. Describe the bracket
   stack, word reversal, and the `ValueError` used for blank required input.
8. **Close with the takeaway:** frontend validation helps the person using the
   form; backend validation protects the application for every client.

Do not use production data or show credentials during the demo.

## Verify the changes

From the `Day16` folder:

```powershell
npm run lint
npm run build
..\Day11\backend\.venv\Scripts\python.exe .\practice_day16.py
```

From the `Day11` folder:

```powershell
.\backend\.venv\Scripts\python.exe -m compileall backend
```

## Project files

```text
Day16/
  src/                 Runnable Day 16 entry reusing CineShelf UI
  practice_day16.py    Required-text validation and Day 16 DSA problems
  README.MD            Learning notes, setup, checks, and presentation guide
  package.json         Frontend scripts and dependencies
  vite.config.js       Vite configuration for the shared app

../Day1314/src/
  App.jsx              Login, role selection, protected dashboard, API errors
  App.css              Shared styles and validation feedback

../Day11/src/
  App.jsx              Controlled movie form and dashboard error handling

../Day11/backend/
  schemas/movie.py     Movie body and poster URL validation
  routes/movie.py      Positive movie IDs and bounded query inputs
```
