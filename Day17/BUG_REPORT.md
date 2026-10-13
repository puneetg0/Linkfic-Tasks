# Day 17 bug report

## Invalid password data caused a server error during login

- **Area:** FastAPI authentication, `POST /auth/login`
- **Severity:** Medium (a damaged account hash prevented that login request from completing normally)
- **Status:** Fixed
- **Reproduction:** In a local test, pass `verify_password` a stored hash with a missing field or a non-numeric iteration count. The regression tests use values such as `not-a-password-hash` and `pbkdf2_sha256$not-a-number$YQ$YQ`.
- **Before the fix:** Splitting the hash into four parts or converting its iteration count to an integer raised `ValueError`. The exception escaped the login route, which could return HTTP 500.
- **Expected behavior:** Treat an unreadable stored hash like an incorrect password. The existing login route should return HTTP 401 without revealing password-storage details.
- **Root cause:** `verify_password` assumed every stored hash had the exact format created by the password-hashing function.
- **Fix:** Validate the hash format, iteration count, salt, and digest before checking the password. Return `False` for malformed values; keep constant-time digest comparison for valid hashes.
- **Regression coverage:** `test_day17.py` checks malformed hashes directly and confirms the login handler rejects one with HTTP 401. It also checks valid and incorrect passwords.

Do not change a real user's password hash or database to reproduce this. The regression test uses an in-memory fake user.
