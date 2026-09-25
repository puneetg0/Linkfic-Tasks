# Day 4 - Python Fundamentals

## **Objective**

The objective of Day 4 was to strengthen Python programming fundamentals and apply the concepts through practical coding exercises. The main goal was to understand how Python concepts work and use them to build a simple Student Management CLI application.

---

## **Tasks Assigned**

The Day 4 tasks focused on learning Python variables, data types, functions, loops, OOP basics, exception handling, and file handling. The practical tasks included building a Student Management CLI and solving basic programming and DSA problems such as Prime Number, Armstrong Number, Binary Search, and Second Largest Number.

---

## **Python Fundamentals**

Python fundamentals are the basic building blocks required to write Python programs. These concepts were practiced before moving to the larger Student Management project.

### **Variables**

Variables are used to store information in a program. For example, a student's name, age, or marks can be stored inside variables.

```python
name = "Puneet"
age = 28
marks = 85
```

### **Data Types**

Data types tell Python what kind of information is being stored.

The main types practiced were:

* String
* Integer
* Float
* Boolean
* List
* Dictionary

Example:

```python
name = "Puneet"
age = 28
marks = 85.5
passed = True
```

### **Functions**

Functions are reusable blocks of code. They help organize a program and prevent writing the same code repeatedly.

Example:

```python
def add(a, b):
    return a + b
```

A function can receive input through parameters and return a result.

### **Loops**

Loops are used when we need to repeat an operation multiple times.

Two main loops were practiced:

* `for` loop
* `while` loop

For example, a `for` loop can be used to go through every student in a list.

### **OOP Basics**

Object-Oriented Programming is a way of organizing programs using classes and objects.

The basic concepts learned were:

* Class
* Object
* `__init__()`
* `self`
* Attributes
* Methods

A class can be thought of as a blueprint, while an object is an actual item created from that blueprint.

### **Exception Handling**

Exception handling is used to handle errors without stopping the entire program.

Python uses `try` and `except` for this purpose.

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number.")
```

This is useful when users enter invalid information.

### **File Handling**

File handling allows a Python program to store or read information from files.

The basic operations practiced were:

* Reading files
* Writing files
* Appending data

Common file modes include:

```text
r → Read
w → Write
a → Append
```

### **JSON**

JSON stands for JavaScript Object Notation. It is a common format for storing and exchanging structured data.

Example:

```json
{
    "name": "Puneet",
    "age": 28,
    "marks": 85
}
```

JSON is commonly used when working with APIs because it allows applications to exchange structured information.

---

# **DSA / Coding Practice**

The DSA practice was used to improve logical thinking and understand how programming problems can be solved step by step.

## **Prime Number**

A prime number is a number that is divisible only by `1` and itself.

Examples:

```text
2
3
5
7
11
13
```

The program checks how many numbers can divide the given number and uses that information to determine whether it is prime.

---

## **Armstrong Number**

An Armstrong number is a number where the sum of each digit raised to the power of the number of digits is equal to the original number.

For example:

```text
153
```

Since it has three digits:

```text
1³ + 5³ + 3³
```

The calculation is:

```text
1 + 125 + 27 = 153
```

Because the result is the original number, `153` is an Armstrong number.

This exercise helped practice loops, digit extraction, arithmetic operations, and conditions.

---

## **Binary Search**

Binary Search is a searching algorithm used to find an element in a sorted list.

Instead of checking every element one by one, Binary Search checks the middle element and eliminates half of the remaining search area.

Example:

```text
10 20 30 40 50 60 70 80 90
```

If we search for `70`, the algorithm first checks the middle value and then decides whether to search on the left or right side.

This exercise helped improve understanding of:

* Lists
* Indexing
* `while` loops
* Conditions
* Search logic

---

## **Second Largest Number**

The Second Largest Number problem requires finding the second highest value from a list.

Example:

```python
numbers = [10, 50, 20, 80, 30]
```

The result is:

```text
Largest: 80
Second Largest: 50
```

This exercise helped practice loops, comparisons, variables, and conditional logic.

---

# **Student Management CLI**

## **Project Overview**

The Student Management CLI is a command-line application built using Python.

CLI means Command Line Interface. Instead of using a graphical interface with buttons and screens, the user interacts with the application through the terminal.

The project combines several Python concepts learned during Day 4.

---

## **Features Implemented**

The application provides four main student management operations:

### **Add Student**

Allows the user to enter a student's:

* Name
* Age
* Marks

The information is then stored in the student list.

### **View Students**

Displays all students currently stored in the application.

### **Search Student**

Allows the user to enter a student name and search for that student in the stored data.

### **Delete Student**

Allows the user to enter a student name and remove the matching student from the list.

---

## **Data Structure Used**

Student information is stored using a Python dictionary.

Example:

```python
student = {
    "name": name,
    "age": age,
    "marks": marks
}
```

Multiple student dictionaries are stored inside a list.

This provides a simple way to manage multiple student records.

---

## **CLI Menu**

The application provides a simple menu:

```text
--- Student Management System ---

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit

Enter your choice:
```

The user selects an option, and the corresponding function is executed.

---

# **Changes Made**

The following changes were completed during Day 4:

* Added Python variables and data type practice.
* Added function-based programming practice.
* Added `for` and `while` loop practice.
* Learned basic OOP concepts.
* Practiced exception handling.
* Practiced file handling.
* Learned JSON structure.
* Added Prime Number practice.
* Added Armstrong Number practice.
* Implemented Binary Search.
* Implemented Second Largest Number.
* Built Student Management CLI.
* Added Add, View, Search, and Delete operations.
* Created Day 4 README.
* Updated the GitHub repository.

---

# **Measurable Impact**

The Day 4 work resulted in measurable practical improvements.

| Area                | Outcome                                 |
| ------------------- | --------------------------------------- |
| Python Fundamentals | Practiced 7+ core concepts              |
| DSA                 | Completed 4 coding problems             |
| Algorithms          | Implemented Binary Search               |
| Problem Solving     | Practiced number and searching problems |
| CLI Development     | Built 1 Student Management application  |
| Student Operations  | Implemented 4 operations                |
| OOP                 | Learned classes and objects             |
| Error Handling      | Practiced `try` and `except`            |
| File Handling       | Practiced file read/write concepts      |
| JSON                | Learned structured data representation  |
| Documentation       | Created Day 4 README                    |
| Version Control     | Updated GitHub repository               |

---

# **Key Learnings**

By completing Day 4, I improved my understanding of Python programming and basic problem-solving.

The major learnings were:

* How variables store information.
* How different Python data types work.
* How functions make code reusable.
* How loops repeat operations.
* How lists and dictionaries store data.
* How classes and objects work.
* How exception handling prevents program crashes.
* How Python works with files.
* How JSON represents structured data.
* How Binary Search works.
* How to solve basic DSA problems.
* How to build a simple CLI application.
* How to organize code into separate functions.

---

# **Challenges Faced**

The main challenges during Day 4 were understanding loops step by step, understanding the difference between classes and objects, understanding the purpose of `self`, implementing Binary Search logic, and finding the second largest number without simply sorting the list.

Another challenge was understanding how multiple functions can work together to create a complete CLI application.

These challenges were addressed by breaking each concept into smaller examples and practicing them individually before combining them into the project.

---

# **Project Structure**

The Day 4 work was organized as follows:

```text
Day4/
│
├── README.md
├── student_management.py
└── dsa_practice.py
```

`student_management.py` contains the Student Management CLI, while `dsa_practice.py` contains the DSA and coding exercises.

---

# **Git Commands Used**

The following Git commands were used to track and upload the Day 4 work:

```bash
git status
git add .
git commit -m "Complete Day 4 Python fundamentals"
git push
```

`git status` was used to check changes, `git add` staged the files, `git commit` created a version of the work, and `git push` uploaded the changes to GitHub.

---

# **Deliverables Completed**

The following Day 4 deliverables were completed:

* Python Fundamentals practice
* Variables and Data Types
* Functions
* Loops
* OOP Basics
* Exception Handling
* File Handling
* JSON learning
* Prime Number
* Armstrong Number
* Binary Search
* Second Largest Number
* Student Management CLI
* Updated README
* Updated GitHub Repository

---

# **Day 4 Outcome**

Day 4 helped strengthen Python fundamentals through practical coding and DSA exercises.

The Student Management CLI brought multiple concepts together into one working application. This provided practical experience with user input, functions, loops, conditions, lists, dictionaries, and basic application structure.

The DSA exercises also improved logical thinking and helped build a foundation for solving programming problems step by step.
