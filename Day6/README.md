I am a complete beginner learning Python backend development.

I am working on **Day 6 of my internship learning tasks**. I want to build a small beginner-friendly **FastAPI Student API project** and complete all the assigned tasks below.

## Day 6 Tasks

### FastAPI

* Install FastAPI
* Learn FastAPI project structure
* Learn routing
* Create basic APIs
* Learn GET requests
* Learn POST requests
* Understand path parameters
* Understand request body
* Use Pydantic BaseModel
* Run the FastAPI application using Uvicorn

### REST API and HTTP

* Understand what an API is
* Understand REST APIs
* Understand HTTP methods
* Understand GET
* Understand POST
* Understand PUT
* Understand DELETE
* Understand JSON
* Understand client-server communication
* Understand request and response

### Postman

* Test GET API
* Test GET API with path parameter
* Test POST API
* Send JSON request body
* Understand API response

### Frontend

* Understand what Fetch API is
* Understand how JavaScript communicates with FastAPI
* Show a simple Fetch API example

### Python / DSA

Practice:

1. Reverse a List
2. Find Maximum Number
3. Merge Two Sorted Arrays
4. Remove Duplicates

### Deliverables

* FastAPI project
* Working APIs
* Postman collection
* requirements.txt
* README.md
* GitHub-ready project

---

## Project Requirements

Create a project called:

**Student API**

Use this beginner-friendly structure:

```text
Day6/
│
├── main.py
├── dsa_practice.py
├── requirements.txt
└── README.md
```

Do NOT use a database for this project. Store students temporarily in a Python list/dictionary so I can understand the basics first.

Create these APIs:

### 1. Home API

```text
GET /
```

Response:

```json
{
    "message": "Welcome to Student API"
}
```

### 2. Get All Students

```text
GET /students
```

Return all students.

Use sample data such as:

```text
Puneet, age 28
Rahul, age 25
```

### 3. Get One Student

```text
GET /students/{student_id}
```

Use a path parameter.

If the student exists, return the student.

If the student does not exist, return a clear message.

### 4. Create Student

```text
POST /students
```

Use Pydantic `BaseModel`.

The request body should look like:

```json
{
    "name": "Amit",
    "age": 24
}
```

Create an ID automatically and add the student to the list.

---



Problems:

### Problem 1

Reverse a List.

Example:

```text
Input:
[1, 2, 3, 4, 5]

Output:
[5, 4, 3, 2, 1]
```

Prefer a loop-based solution first.

### Problem 2

Find Maximum Number.

Example:

```text
Input:
[10, 25, 7, 40, 15]

Output:
40
```

Prefer a loop-based solution first.

### Problem 3

Merge Two Sorted Arrays.

Example:

```text
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

Output:
[1, 2, 3, 4, 5, 6]
```

Explain the two-pointer idea in very simple language.

### Problem 4

Remove Duplicates.

Example:

```text
Input:
[1, 2, 2, 3, 3, 4]

Output:
[1, 2, 3, 4]
```

Use a simple beginner-friendly approach first.

---

## Postman Testing

Show me exactly how to test each API in Postman.

For every API tell me:

* HTTP method
* URL
* Whether I need Params
* Whether I need Body
* What JSON to enter
* Expected response

For POST, explain:

```text
Body
→ raw
→ JSON
```

and show exactly what JSON I should enter.

---

## Fetch API

After FastAPI is working, explain this simple concept:

```text
JavaScript
    ↓
fetch()
    ↓
FastAPI
    ↓
JSON response
    ↓
JavaScript
```

Give me a simple JavaScript example that calls:

```text
GET /students
```

Do not introduce React yet.

---

## README Requirements

At the end, create a complete `README.md` with proper Markdown headings.

Include:

# Day 6 - FastAPI and REST API

## Objective

## Tasks Assigned

## Technologies Used

## Project Structure

## FastAPI Installation

## How to Run the Project

## API Endpoints

Include a table:

| Method | Endpoint                 | Purpose          |
| ------ | ------------------------ | ---------------- |
| GET    | `/`                      | Welcome message  |
| GET    | `/students`              | Get all students |
| GET    | `/students/{student_id}` | Get one student  |
| POST   | `/students`              | Create student   |

## REST API Concepts

## HTTP Methods

## JSON

## Client-Server Communication

## Postman Testing

## Fetch API

## DSA Practice

## What I Learned

## Deliverables

Keep the README professional and suitable for an internship GitHub repository.

---

## GitHub

After the project is complete, explain these commands:

```bash
git status
git add .
git commit -m "Complete Day 6 FastAPI project"
git push origin main
```

Explain what each command does in beginner-friendly language.

Also show me how to check:

```bash
git status
```

and confirm that the working tree is clean.

---

## Important Rules

* Teach me slowly.
* Assume I am a beginner.
* Use simple English.
* Do not skip basic concepts.
* Do not give advanced code unnecessarily.
* Explain the reason behind each important line.
* Give code that I can directly copy and run.
* Tell me exactly which file each code block belongs to.
* Do not move to the next step until the current step is understandable.
* If there is an error, help me debug it step by step.
* Keep the project small enough that I can explain it in an internship interview.
* At the end, give me a short list of questions an interviewer may ask about this Day 6 project.














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
