# CineShelf API Reference

This document describes the FastAPI routes implemented by the CineShelf backend. For an interactive version, start the backend and open [Swagger UI](http://localhost:8000/docs) or [ReDoc](http://localhost:8000/redoc).

## Base URL

Local development:

```text
http://localhost:8000
```

Requests and responses use JSON except for `204 No Content` responses.

## Authentication

Registration and login are public. Other routes require a bearer access token:

```http
Authorization: Bearer <access_token>
```

The token is returned by `POST /auth/login` and expires after 30 minutes. Send it in the authorization header; do not send it as a URL query parameter. Regular users can access only their own movies. The administrator routes require an account whose role is `admin`.

## Account endpoints

### `POST /auth/register`

Creates a regular user account.

Request:

```json
{
  "email": "reader@example.com",
  "password": "a-long-password"
}
```

Email is trimmed and lowercased. Password length must be 8–128 characters.

Responses:

- `201 Created` — account created; returns `id`, normalized `email`, and `role`.
- `409 Conflict` — an account with that email already exists.
- `422 Unprocessable Entity` — request fields are invalid.

Public registration does not allow a caller to choose an administrator role.

### `POST /auth/login`

Checks credentials and issues an access token.

Request:

```json
{
  "email": "reader@example.com",
  "password": "a-long-password"
}
```

Successful response (`200 OK`):

```json
{
  "access_token": "<signed-token>",
  "token_type": "bearer",
  "expires_in": 1800
}
```

Returns `401 Unauthorized` for an incorrect email or password and `422 Unprocessable Entity` for invalid request data.

### `GET /auth/me`

Requires authentication. Returns the current user's `id`, `email`, and `role`.

## Movie endpoints

Movie request fields:

| Field | Type | Rules |
|---|---|---|
| `title` | string | Required; trimmed; 1–120 characters; cannot be blank. |
| `genre` | string | Required; trimmed; 1–40 characters; cannot be blank. |
| `release_year` | integer | Required; between 1888 and 2100. |
| `rating` | number | Required; between 0 and 10 inclusive. |
| `watched` | boolean | Optional; defaults to `false`. |
| `poster_url` | string or `null` | Optional; maximum 2048 characters; if supplied, must be an HTTP or HTTPS URL. |

Example:

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

Responses for movie resources also contain `id` and `owner_id`.

### `GET /movies`

Requires authentication. Lists the current user's movies ordered by ID. Optional query parameters:

- `search` — title search, up to 120 characters.
- `genre` — exact genre filter (case-insensitive), up to 40 characters.

Example:

```text
GET /movies?search=arr&genre=Science%20Fiction
```

Returns `200 OK` with a JSON array. A user who has no matching movies receives an empty array.

### `GET /movies/{movie_id}`

Requires authentication. Returns a movie owned by the current user.

- `200 OK` — movie found.
- `404 Not Found` — movie does not exist or belongs to another user.
- `422 Unprocessable Entity` — ID is not a positive integer.

### `POST /movies`

Requires authentication. Creates a movie for the current user. The `owner_id` is assigned by the API and should not be included in the request.

- `201 Created` — movie created.
- `422 Unprocessable Entity` — fields fail validation.

### `PUT /movies/{movie_id}`

Requires authentication. Replaces the movie's editable fields using the movie request schema.

- `200 OK` — updated movie.
- `404 Not Found` — movie does not exist or belongs to another user.
- `422 Unprocessable Entity` — ID or fields are invalid.

### `PATCH /movies/{movie_id}/watched`

Requires authentication. Updates only the watched status.

Request:

```json
{
  "watched": true
}
```

- `200 OK` — updated movie.
- `404 Not Found` — movie does not exist or belongs to another user.
- `422 Unprocessable Entity` — invalid ID or request.

### `DELETE /movies/{movie_id}`

Requires authentication.

- `204 No Content` — movie deleted.
- `404 Not Found` — movie does not exist or belongs to another user.
- `422 Unprocessable Entity` — ID is not a positive integer.

### `GET /genres`

Requires authentication. Returns the distinct genres in the current user's collection as a sorted JSON array of strings.

## Administrator endpoints

These endpoints require a valid bearer token for a user with the `admin` role. Normal users receive `403 Forbidden`.

### `GET /admin/users`

Returns users ordered by ID. Each entry includes `id`, `email`, and `role`; password hashes are never included.

### `GET /admin/movies`

Returns movies across all users, with the movie data and `owner_email`. Legacy movies without an owner can have a `null` owner email.

## Health endpoint

### `GET /health`

Runs a simple database query and returns:

```json
{
  "status": "ok"
}
```

If the database query fails, the endpoint returns an error rather than reporting the service healthy.

## Error responses

FastAPI validation errors use `422 Unprocessable Entity`. Authentication failures use `401 Unauthorized`; insufficient administrator permissions use `403 Forbidden`; missing or inaccessible movies use `404 Not Found`. Duplicate registration uses `409 Conflict`.

Validation error details use FastAPI's standard `detail` array, including the field location and validation message. Clients should rely on the HTTP status and `detail`, not on undocumented wording.
