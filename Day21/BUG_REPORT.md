# Day 21 bug report - CineShelf release preparation

## 1. Login could spend too long checking a damaged password record

- **Status:** Fixed and regression-tested.
- **Severity:** Medium.
- **Area:** `POST /auth/login`, password hash verification.
- **What could happen:** The saved password format includes the number of PBKDF2 rounds. Before the fix, a positive but enormous number was accepted. If such a value was stored, a login could keep the server busy for an unreasonable time.
- **Fix:** Accept only the current supported range of 600,000 through 1,000,000 rounds. Values outside that range are treated as a bad password record.
- **Test:** `test_password_verifier_rejects_corrupt_or_excessive_iteration_hashes`.

## 2. Health check did not check the database

- **Status:** Fixed and regression-tested.
- **Severity:** Medium.
- **Area:** `GET /health`.
- **What could happen:** The route returned `{"status":"ok"}` without contacting the database. A deployment system could therefore see a healthy response even when the API could not read or write its data.
- **Fix:** The route now executes `SELECT 1` using the database session.
- **Test:** `test_health_endpoint_checks_database_connection`.

## 3. Deployed frontend origins were not configurable

- **Status:** Fixed in code; a real deployment still needs its own value.
- **Severity:** Medium.
- **Area:** API CORS configuration.
- **What could happen:** Browsers only allow a website to call an API on another domain if the API permits that website's origin. Only local development addresses were allowed.
- **Fix:** The API now reads a comma-separated `CORS_ORIGINS` allowlist from the environment. Production must list its exact frontend origin(s); do not use an open wildcard.
- **Verification needed:** Test the actual frontend domain and API domain after deployment.

## 4. API regressions were not covered by automated tests

- **Status:** Addressed with tests.
- **Severity:** Medium.
- **Area:** Authentication, movie API, and administrator API.
- **What could happen:** Changes to sign-in, data ownership, validation, or roles could break without a repeatable check.
- **Fix:** Added API regression tests using a temporary SQLite database. They cover registration, login, unauthorized requests, validation, movie CRUD, ownership boundaries, administrator permissions, and token expiry.
- **Test command:** `python -m pytest Day18\tests Day21\test_day21.py -q`.

## 5. The signed-in navigation overflowed on narrow phones

- **Status:** Fixed and checked in a browser.
- **Severity:** Medium.
- **Area:** Responsive layout of the signed-in movie library.
- **What could happen:** At a 320-pixel mobile viewport, the brand, three navigation links, sign-out button, and add-movie button were forced into one row. The page became wider than the screen and some controls were pushed off-screen.
- **Fix:** At phone widths, the header now uses two rows: the brand and account actions on the first row, and the navigation links on the second.
- **Verification:** No horizontal overflow was observed at 320, 375, 768, or 1280 CSS-pixel widths after the fix.

## Release limitations to keep visible

The code changes and tests do not replace a staging deployment. The current app still needs database migrations for production schema changes, a secure administrator setup procedure, and tested deployment secrets and domains. The Docker Compose file passed configuration validation, but the images could not be built in this environment because the Docker daemon was not running.
