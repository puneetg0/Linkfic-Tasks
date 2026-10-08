# Day 10 - CineShelf FastAPI Backend

## Overview

Day 10 continues the CineShelf movie collection project by building and organizing a FastAPI backend, connecting it to the React frontend, and practicing API and DSA concepts.

The API supports creating, reading, updating, and deleting movies. Movie data is stored in `backend/movies.json`, so changes are retained when the server restarts.

## Tasks

- Create CRUD APIs.
- Learn API routing.
- Organize the backend folder structure.
- Create movie models and request/response schemas.
- Test API endpoints using Postman.
- Connect React with FastAPI.

## Project Structure

```text
backend/
├── main.py             # Creates the FastAPI app, middleware, and route registration
├── models/
│   └── movie.py        # Typed movie record definitions
├── schemas/
│   └── movie.py        # Request validation and API response schemas
├── routes/
│   └── movie.py        # Movie and genre API endpoints
├── data/
│   └── movies.py       # Seed data and JSON-backed movie storage
├── movies.json         # Persisted movie collection (created on first run)
└── requirements.txt    # FastAPI and Uvicorn dependencies
```

### What each part does

- **`main.py`** creates the FastAPI application, configures CORS for the Vite frontend, adds the health endpoint, and includes the movie router.
- **Models** describe the shape of movie records used by the application.
- **Schemas** validate incoming movie data and define the API's response format.
- **Routes** connect HTTP methods and URL paths to movie operations.
- **Data** provides starter movies and functions for loading, saving, and changing the JSON-backed collection.

## API Routes

The backend runs at `http://localhost:8000`. Interactive API documentation is available at `http://localhost:8000/docs`.

| Method | Endpoint | Description | Success response |
|---|---|---|---|
| `GET` | `/health` | Check that the API is running | `200 OK` |
| `GET` | `/genres` | Get the available movie genres | `200 OK` |
| `GET` | `/movies` | Get all movies; optionally filter with `search` and `genre` | `200 OK` |
| `GET` | `/movies/{movie_id}` | Get one movie by ID | `200 OK` |
| `POST` | `/movies` | Add a movie | `201 Created` |
| `PUT` | `/movies/{movie_id}` | Replace a movie's editable fields | `200 OK` |
| `PATCH` | `/movies/{movie_id}/watched` | Change a movie's watched status | `200 OK` |
| `DELETE` | `/movies/{movie_id}` | Delete a movie | `204 No Content` |

Examples of collection filters:

```text
GET /movies?search=dark
GET /movies?genre=Drama
GET /movies?search=the&genre=Comedy
```

### Example request body

Use this JSON body with `POST /movies` or `PUT /movies/{movie_id}`:

```json
{
  "title": "The Example Movie",
  "genre": "Drama",
  "release_year": 2024,
  "rating": 8.2,
  "watched": false,
  "poster_url": null
}
```

The title and genre are trimmed and must not be blank. The year must be between 1888 and 2100, and the rating must be between 0 and 10. `watched` defaults to `false`, and `poster_url` is optional.

For `PATCH /movies/{movie_id}/watched`, send:

```json
{
  "watched": true
}
```

## REST APIs, HTTP Methods, and Status Codes

A REST API exposes resources through URLs and uses standard HTTP methods to describe actions on those resources. In CineShelf, a movie is a resource addressed by `/movies` or `/movies/{movie_id}`.

- **GET** reads a resource and should not change it.
- **POST** creates a resource.
- **PUT** updates a resource's editable fields.
- **PATCH** changes part of a resource, such as its watched status.
- **DELETE** removes a resource.

Common status codes used by this API:

- **200 OK** — the request succeeded.
- **201 Created** — a movie was created.
- **204 No Content** — a movie was deleted successfully; there is no response body.
- **404 Not Found** — the requested movie ID does not exist.
- **422 Unprocessable Content** — request data failed validation.

## Test with Postman

Create a Postman collection named **CineShelf API** and set its base URL to `http://localhost:8000`. Add requests for the routes in the API table above. A useful test sequence is:

1. Send `GET /health` and confirm the response is `200`.
2. Send `GET /movies` and `GET /genres`.
3. Send `POST /movies` with the example JSON body and confirm `201`; note the returned movie ID.
4. Send `GET /movies/{movie_id}` using that ID.
5. Send `PUT /movies/{movie_id}` with the movie fields and confirm the changed response.
6. Send `PATCH /movies/{movie_id}/watched` with `{"watched": true}`.
7. Try `GET /movies?search=example` and `GET /movies?genre=Drama`.
8. Send `DELETE /movies/{movie_id}` and confirm `204`.
9. Request the deleted ID and confirm `404`.

Save the collection and its example requests from Postman if an exported Postman collection is required as a separate deliverable.

## React and FastAPI Integration

The React frontend in `src/App.jsx` calls the FastAPI server at `http://localhost:8000`. It loads and displays movies, and uses the API to add, edit, delete, search, filter, and update watched status. The backend allows requests from the Vite development origins `http://localhost:5173` and `http://127.0.0.1:5173`.

Run the frontend and backend at the same time in separate terminals.

## Run CineShelf on Windows

From the Day10 project root, create and install the backend virtual environment the first time:

```cmd
cd backend
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

With the virtual environment active, start Uvicorn from the Day10 project root. If the terminal is still in `backend`, move up one folder first:

```cmd
cd ..
python -m uvicorn backend.main:app --reload
```

Keep the backend terminal open while using the site. To leave the virtual environment, stop the server with `Ctrl+C` and run:

```cmd
deactivate
```

In a second terminal opened at the Day10 project root, start the frontend:

```cmd
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`.

## YouTube Search

- FastAPI CRUD Tutorial
- FastAPI Project Structure
- Postman API Testing

## Recommended Channels

- Tech With Tim
- freeCodeCamp
- Traversy Media

## Learn Along the Way

- CRUD operations
- API architecture and routing
- HTTP requests and responses
- HTTP methods and status codes
- API testing with Postman

## DSA / Coding Practice

### Python / Backend: Dictionary CRUD Operations

Dictionaries store key-value pairs. The basic CRUD operations are:

```python
movie = {"title": "Arrival", "year": 2016}  # Create
title = movie["title"]                      # Read
movie["year"] = 2017                        # Update
del movie["year"]                           # Delete
```

### Python / Backend: Find the Second Largest Number

This version returns the **second-largest distinct** number and raises a `ValueError` if the input has fewer than two distinct values.

```python
def second_largest(numbers: list[int]) -> int:
    largest = second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number

    if second is None:
        raise ValueError("At least two distinct numbers are required")

    return second


print(second_largest([10, 5, 25, 8, 25]))  # 10
```

Time complexity: **O(n)**. Extra space: **O(1)**.

### Frontend / React: What Is a REST API?

A REST API lets applications exchange data over HTTP using resource URLs and methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`. CineShelf's React frontend sends requests to FastAPI, which validates the requests, performs the requested movie operation, and returns JSON or an HTTP status code.

### Frontend / React: Explain HTTP Methods

In this project, `GET` reads movie data, `POST` adds a movie, `PUT` edits its fields, `PATCH` changes its watched status, and `DELETE` removes it. The frontend uses `fetch()` to send these requests and updates its React state with successful responses.

### Problem Solving / DSA: Merge Sorted Arrays

Given two arrays sorted in ascending order, use two pointers to create one sorted result:

```python
def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    merged = []
    left = right = 0

    while left < len(first) and right < len(second):
        if first[left] <= second[right]:
            merged.append(first[left])
            left += 1
        else:
            merged.append(second[right])
            right += 1

    merged.extend(first[left:])
    merged.extend(second[right:])
    return merged


print(merge_sorted([1, 4, 7], [2, 3, 8]))  # [1, 2, 3, 4, 7, 8]
```

Time complexity: **O(n + m)**. Extra space: **O(n + m)**.

### Problem Solving / DSA: Rotate Array

This function rotates a list to the right by `k` positions. Modulo handles values of `k` larger than the list length.

```python
def rotate_right(numbers: list[int], k: int) -> list[int]:
    if not numbers:
        return numbers

    k %= len(numbers)
    return numbers[-k:] + numbers[:-k] if k else numbers.copy()


print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

Time complexity: **O(n)**. Extra space: **O(n)**.

## Deliverables

- CRUD API completed for the CineShelf movie collection.
- Postman collection with requests covering the API routes.
- GitHub repository updated with the Day 10 work.

## Assigned

- Create and test the CRUD API.
- Keep the backend organized into models, schemas, routes, and data modules.
- Integrate the React site with the FastAPI backend.
- Practice the listed Python and DSA problems.
