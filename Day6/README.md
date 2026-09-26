# Beginner Student API

A small FastAPI project for practicing routes, GET requests, POST requests, path parameters, request bodies, and Pydantic models.

## 1. Install dependencies

Run this from the project folder:

```powershell
python -m pip install -r requirements.txt
```

## 2. Start the API

```powershell
python -m uvicorn main:app --reload
```

Open the interactive API documentation at:

- http://127.0.0.1:8000/docs

## Available routes

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/` | Check that the API is running |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get one student using a path parameter |
| POST | `/students` | Add a student using a JSON request body |

Example JSON for `POST /students`:

```json
{
  "name": "Riya Singh",
  "age": 22,
  "course": "Web Development",
  "email": "riya@example.com"
}
```

The student data is stored in memory, so it resets whenever the server restarts.
