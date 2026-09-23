# Day 4 - Python Fundamentals

## Objective

The objective of Day 4 was to strengthen Python programming fundamentals and apply them through practical coding exercises and a command-line Student Management System.

The main focus areas were:

- Python variables and data types
- Functions
- Loops
- OOP basics
- Exception handling
- File handling
- JSON
- DSA and coding practice
- Student Management CLI
- GitHub and README documentation

---

## Tasks Assigned

### Python Fundamentals

- Learn variables
- Learn data types
- Learn functions
- Learn loops
- Learn OOP basics
- Learn exception handling
- Learn file handling
- Build a Student Management CLI

### YouTube Search

- Python Complete Tutorial
- Python OOP
- Python Exception Handling

### Recommended Channels

- Tech With Tim
- Programming with Mosh
- freeCodeCamp

### Learn Along the Way

- Why Python is popular
- Functions
- OOP
- Modules
- Error Handling

### DSA / Coding Practice

#### Python

- Prime Number
- Armstrong Number

#### Frontend

- Explain JSON

#### DSA

- Binary Search
- Second Largest Number

### Deliverables

- Student Management CLI
- GitHub updated
- README updated

---

# Work Completed

## 1. Python Variables

Learned how variables are used to store data in Python.

Example:

```python
name = "Puneet"
age = 28
marks = 85.5

Practiced creating variables and using them in Python programs.

2. Python Data Types

Learned and practiced the following Python data types:

String
Integer
Float
Boolean
List
Dictionary

Also practiced checking data types using:

type()
3. Functions

Learned how to create reusable blocks of code using functions.

Practiced:

Creating functions
Parameters
Arguments
Return values
Calling functions

Example:

def add(a, b):
    return a + b
4. Loops

Practiced the two main types of Python loops:

For Loop

Used for iterating through lists and repeating operations.

While Loop

Used for repeating operations while a condition is true.

Loops were also used in DSA problems and the Student Management CLI.

5. OOP Basics

Learned the basic concepts of Object-Oriented Programming.

Topics covered:

Class
Object
__init__()
self
Attributes
Methods

The Student example was used to understand how real-world entities can be represented using Python classes and objects.

6. Exception Handling

Learned how to handle runtime errors using:

try
except

Example:

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number.")

This helps prevent programs from crashing because of invalid user input.

7. File Handling

Learned the basics of reading and writing files.

Practiced:

open()

and:

with open(...)

Also learned common file modes:

r - Read
w - Write
a - Append
8. JSON

Learned the basic structure and purpose of JSON.

Example:

{
    "name": "Puneet",
    "age": 28,
    "marks": 85
}

Understood that JSON stores information using key-value pairs and is commonly used for exchanging data between applications and APIs.

DSA / Coding Practice
1. Prime Number

Practiced checking whether a number is a prime number.

The exercise improved understanding of:

Loops
Conditions
Modulus operator
Counters
Number divisibility
2. Armstrong Number

Practiced the logic behind Armstrong numbers.

For example:

153 = 1³ + 5³ + 3³
153 = 153

This exercise provided practice with:

Loops
Arithmetic operations
Conditions
Number manipulation
3. Binary Search

Implemented Binary Search on a sorted list.

Example:

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

The algorithm searches for a value by checking the middle element and reducing the search area.

Practiced:

List indexing
while loops
left pointer
right pointer
Middle index
Conditional statements
4. Second Largest Number

Implemented a solution to find the second largest number from a list.

Example:

numbers = [10, 50, 20, 80, 30]

Result:

Largest: 80
Second Largest: 50

Practiced:

Lists
Variables
Comparisons
for loops
Conditional statements
Student Management CLI
Project Overview

Built a command-line Student Management System using Python.

The application allows users to manage student information through a terminal-based menu.

Features Implemented

The CLI includes the following features:

Add Student
View Students
Search Student
Delete Student
Exit
Student Information

The application stores:

Student Name
Student Age
Student Marks

Student information is represented using Python dictionaries and stored inside a list.

Example:

student = {
    "name": name,
    "age": age,
    "marks": marks
}
Example CLI Menu
--- Student Management System ---

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit

Enter your choice:
Changes Made
Python Development
Added Python fundamentals practice.
Added variable and data type examples.
Added function-based programs.
Added for and while loop practice.
Practiced basic OOP concepts.
Practiced exception handling.
Practiced file handling.
Learned JSON data structure.
DSA Practice
Added Prime Number practice.
Added Armstrong Number practice.
Added Binary Search implementation.
Added Second Largest Number implementation.
Project Development
Created Student Management CLI.
Added student creation functionality.
Added student viewing functionality.
Added student search functionality.
Added student deletion functionality.
Added command-line menu system.
Documentation
Created Day 4 README.
Documented assigned tasks.
Documented completed work.
Documented project features.
Documented DSA practice.
Updated GitHub repository.
Measurable Impact
Area	Measurable Outcome
Python Fundamentals	Practiced 7+ core Python concepts
DSA Practice	Completed 4 coding problems
Search Algorithms	Implemented 1 Binary Search algorithm
Problem Solving	Practiced Prime, Armstrong, and Second Largest problems
CLI Development	Built 1 Student Management CLI
Student Operations	Implemented 4 core operations
OOP	Practiced classes, objects, __init__(), and self
Error Handling	Practiced try and except
File Handling	Practiced reading and writing files
JSON	Learned JSON structure and key-value data
Documentation	Created and updated Day 4 README
Version Control	Updated GitHub repository
Key Learnings

By the end of Day 4, I improved my understanding of:

Python variables
Python data types
Functions
Function parameters and return values
for loops
while loops
Lists
Dictionaries
Classes and objects
__init__()
self
Exception handling
File handling
JSON
Binary Search
Second Largest Number
Basic problem-solving
Command-line application development
GitHub documentation
Challenges Faced

The main challenges during Day 4 were:

Understanding how loops execute step by step.
Understanding the difference between classes and objects.
Understanding the purpose of self.
Understanding how Binary Search reduces the search area.
Understanding how to track the largest and second largest values.
Understanding how multiple functions work together in a CLI application.
Understanding how dictionaries and lists can be used to store student information.

These challenges were addressed by breaking each concept into smaller examples and implementing them through practical exercises.

Project Structure
Day4/
│
├── README.md
├── student_management.py
└── dsa_practice.py
Git Commands Used

The Day 4 changes were prepared and pushed to GitHub using:

git status
git add .
git commit -m "Complete Day 4 Python fundamentals"
git push
Deliverables Completed

The following Day 4 deliverables were completed:

Python fundamentals practice
Variables and data types
Functions
Loops
OOP basics
Exception handling
File handling
JSON learning
Prime Number practice
Armstrong Number practice
Binary Search implementation
Second Largest Number implementation
Student Management CLI
Day 4 README
GitHub repository update
Day 4 Outcome

Day 4 focused on strengthening Python fundamentals and applying them through practical programming.

The Student Management CLI combined multiple concepts learned during the day, including variables, lists, dictionaries, functions, loops, conditions, and user input.

The DSA exercises provided additional practice with programming logic, searching techniques, and problem-solving.

Overall, Day 4 helped build a stronger foundation in Python programming and prepared the groundwork for developing more structured applications in the upcoming internship tasks.
