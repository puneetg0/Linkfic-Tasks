from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str
    email: str


students = [
    Student(
        name="Aarav Sharma",
        age=20,
        course="Python",
        email="aarav@example.com",
    ),
    Student(
        name="Meera Patel",
        age=21,
        course="FastAPI",
        email="meera@example.com",
    ),
]


@app.get("/")
def home():
    return {"message": "Welcome to the Student API"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < 1 or student_id > len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id - 1]


@app.post("/students", status_code=201)
def add_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student_id": len(students),
        "student": student,
    }
