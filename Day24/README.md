# Day 24 – FastAPI CRUD APIs and Database Integration

## 1. Task Overview

**Task Title:** FastAPI CRUD Operations and Database Integration

**Task Type:** Backend Development

**Technology Stack:** Python, FastAPI, SQLAlchemy, PostgreSQL, Postman, Git, and GitHub

**Task Status:** Completed

## 2. Task Assigned

The main objective of this task was to develop backend functionality using FastAPI, connect the application to a database, implement CRUD operations, validate incoming API requests, and organize the backend code into separate modules.

### Assigned Tasks

- Create database models.
- Develop CRUD APIs.
- Connect the database.
- Test APIs using Postman.
- Handle API validation.
- Organize backend modules.

## 3. Introduction

In this task, I worked on building backend functionality using FastAPI and integrating it with a database. I focused on understanding how a backend application receives requests, processes data, communicates with a database, and returns responses to the frontend.

I implemented CRUD operations, which are used to create, read, update, and delete records. I also worked on database models, API validation, testing with Postman, and organizing the backend project structure.

This task helped me understand how a backend application manages data and how REST APIs connect the frontend with the database.

## 4. Detailed Explanation of Completed Tasks

### Task 1: Create Database Models

**Status: Completed**

#### What I Learned

A database model defines the structure of the data that an application stores in a database. It describes the fields, data types, and relationships that are used to organize information.

I used SQLAlchemy to define database models in Python. SQLAlchemy is an Object-Relational Mapper (ORM) that allows me to interact with database tables using Python classes and objects instead of writing every database query manually.

#### What I Implemented

- Created database models using SQLAlchemy.
- Defined fields and appropriate data types for storing records.
- Configured primary keys to uniquely identify records.
- Used suitable column definitions and constraints.
- Understood how Python classes represent database tables.
- Connected model definitions with the database configuration.

#### Example

For a task management application, a task model may contain:

- `id`: Unique identifier for each task.
- `title`: Name of the task.
- `description`: Details about the task.
- `status`: Current status of the task.
- `created_at`: Date and time when the task was created.

#### Outcome

I completed the database model setup and understood how application data is structured before it is stored in the database.

### Task 2: Develop CRUD APIs

**Status: Completed**

#### What I Learned

CRUD stands for Create, Read, Update, and Delete. These are the four basic operations used to manage data in most backend applications.

I used FastAPI to develop REST API endpoints that allow the application to perform these operations.

#### What I Implemented

**1. Create**

I implemented an API to add a new record to the database. The API accepts the required information, validates the request data, and saves the new record.

**2. Read**

I implemented APIs to retrieve stored records. These APIs allow the application to fetch all available records or retrieve a specific record using its unique ID.

**3. Update**

I implemented an API to modify an existing record. The API identifies the record and updates the required fields.

**4. Delete**

I implemented an API to remove a record from the database using its unique ID.

#### Common HTTP Methods

| HTTP Method | Purpose | Example |
|---|---|---|
| POST | Create a record | Add a new task |
| GET | Read records | View saved tasks |
| PUT | Update a record | Replace task details |
| PATCH | Partially update a record | Change task status |
| DELETE | Delete a record | Remove a task |

The actual HTTP methods depend on the endpoints implemented in the application.

#### Outcome

I completed the CRUD API implementation and understood how HTTP requests are used to manage database records through a backend application.

### Task 3: Connect the Database

**Status: Completed**

#### What I Learned

A database connection allows the backend application to communicate with a database for storing, retrieving, updating, and deleting information.

I worked on connecting the FastAPI application with the database using SQLAlchemy.

PostgreSQL is a relational database management system that stores structured information in tables. SQLAlchemy provides the interface between Python code and the database.

#### What I Implemented

- Configured the database connection.
- Set up the SQLAlchemy database engine and session management.
- Connected database models with the database.
- Used database sessions to perform CRUD operations.
- Understood how database queries are executed from the backend.
- Worked with the database configuration required by the application.

#### Database Workflow

1. The client sends an API request.
2. FastAPI receives the request.
3. The backend processes the request.
4. SQLAlchemy communicates with the database.
5. The database performs the requested operation.
6. FastAPI returns the appropriate response to the client.

#### Outcome

I completed the database integration and understood how a FastAPI application communicates with a relational database.

### Task 4: Test APIs Using Postman

**Status: Completed**

#### What I Learned

Postman is an API testing tool that allows me to send HTTP requests to backend endpoints and inspect their responses without needing a frontend application.

I used Postman to test the API functionality and check whether the endpoints returned the expected results.

#### What I Implemented

- Sent POST requests to create records.
- Sent GET requests to retrieve records.
- Sent PUT or PATCH requests to update records.
- Sent DELETE requests to remove records.
- Checked response status codes and response bodies.
- Tested request payloads using JSON.
- Checked how the APIs handled invalid inputs and missing records.
- Verified that database changes were reflected in subsequent requests.

#### Important HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 OK | Request completed successfully |
| 201 Created | A new record was created |
| 204 No Content | Request succeeded without a response body |
| 400 Bad Request | Request contains an invalid operation or data |
| 404 Not Found | Requested resource was not found |
| 422 Unprocessable Content | Request data failed validation |
| 500 Internal Server Error | An unexpected server-side error occurred |

The exact status code depends on the API implementation.

#### Outcome

I completed API testing using Postman and verified the implemented CRUD operations, request formats, and responses.

### Task 5: Handle API Validation

**Status: Completed**

#### What I Learned

API validation ensures that incoming data follows the expected format and rules before the backend processes it.

FastAPI uses Pydantic models to validate request data. Validation helps prevent invalid or incomplete information from entering the application.

#### What I Implemented

- Defined request schemas for incoming data.
- Specified expected field types, such as strings and integers.
- Checked required fields in API requests.
- Used validation rules to restrict invalid input.
- Tested requests containing missing or incorrect values.
- Reviewed validation error responses returned by FastAPI.
- Understood the importance of validating data before database operations.

#### Example

For a task creation API, the title should contain text rather than an unexpected data type. If a required field is missing or has an invalid value, the API should return an appropriate validation error.

#### Why Validation Is Important

- Maintains data consistency.
- Prevents invalid request data from being processed.
- Makes APIs easier to use and debug.
- Helps return meaningful error responses.
- Improves the reliability of the application.

#### Outcome

I completed the API validation tasks and understood how FastAPI and Pydantic help maintain the quality and correctness of incoming data.

### Task 6: Organize Backend Modules

**Status: Completed**

#### What I Learned

Backend modularization means dividing an application into smaller files and modules based on their responsibilities. This makes the code easier to understand, test, maintain, and extend.

Instead of writing all the application logic in one file, I organized the backend into separate modules for different functions.

#### What I Implemented

- Organized the FastAPI application into logical modules.
- Separated API routes from database models.
- Kept request and response schemas separate from database models.
- Organized database connection and session configuration.
- Separated business logic where appropriate.
- Used imports to connect the modules.
- Improved code readability and maintainability.

#### Example Backend Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       └── tasks.py
├── requirements.txt
└── README.md
```

This is an example of a modular FastAPI structure. The exact file names and folders may vary according to the project.

#### Outcome

I completed the backend organization task and understood how modular code helps manage larger applications more efficiently.

## 5. Learning Resources


## 6. Learn Along the Way

### API Design

I learned that API design involves defining endpoints, HTTP methods, request formats, response structures, and status codes.

A well-designed API should have clear endpoint names, consistent responses, appropriate HTTP methods, and useful error messages.

### Database Relationships

I learned the basic purpose of database relationships and how tables can be connected using keys.

- **One-to-one:** One record is associated with one related record.
- **One-to-many:** One record can be associated with multiple related records.
- **Many-to-many:** Multiple records can be associated with multiple records in another table.

Primary keys identify records, while foreign keys connect related records. Understanding these concepts helps when designing databases for real-world applications.

### Backend Architecture

I learned how different backend components work together:

- Routes receive incoming requests.
- Schemas validate request and response data.
- Models define database table structures.
- CRUD functions perform database operations.
- Database configuration manages connections and sessions.
- The main application initializes FastAPI and registers routes.

Separating these responsibilities makes backend code easier to maintain and expand.

### Validation

I learned that validation checks whether incoming data meets the application's requirements. It helps catch incorrect field types, missing values, and other invalid inputs before they cause problems in later stages of processing.

## 7. DSA and Coding Practice

### Python / Backend: CRUD Logic

I practiced understanding CRUD logic and how it can be implemented using Python functions.

The main concepts included:

- Creating new records.
- Retrieving individual or multiple records.
- Updating existing data.
- Deleting records.
- Handling records that do not exist.
- Returning suitable responses after database operations.

This practice helped me connect Python programming concepts with real backend application development.

### Frontend / React: API Consumption Concepts

I reviewed how a React frontend communicates with a FastAPI backend.

The main concepts included:

- Sending HTTP requests from React.
- Using `fetch()` or Axios to communicate with API endpoints.
- Sending JSON request data.
- Reading JSON responses.
- Displaying backend data in UI components.
- Handling loading states and API errors.
- Updating the UI after creating, editing, or deleting records.

I understood that the frontend handles user interaction, while the backend processes requests and manages application data.

### Problem Solving / DSA: Hash Map Implementation

I practiced the concept of a hash map, which stores data as key-value pairs and allows efficient lookups.

In Python, a dictionary is commonly used to implement hash-map-based solutions.

#### Example

```python
student = {
    "id": 101,
    "name": "Aman",
    "course": "Python"
}

print(student["name"])
```

**Output:**

```text
Aman
```

This example demonstrates how a value can be retrieved using its key.

I learned that hash maps are useful for:

- Fast lookups by key.
- Counting the frequency of elements.
- Removing duplicate values.
- Storing and retrieving structured information.
- Solving common coding interview problems.

Average-case dictionary lookup is typically \(O(1)\), although performance can vary depending on the operation and collisions.

## 8. Deliverables Completed

| Deliverable | Status | Description |
|---|---|---|
| CRUD APIs | Completed | Implemented create, read, update, and delete operations |
| Database connection | Completed | Connected the backend with the configured database |
| Postman testing | Completed | Tested API endpoints and checked responses |
| API validation | Completed | Implemented and tested request validation |
| Backend structure | Completed | Organized application code into logical modules |
| GitHub update | Completed | Updated the project repository with the completed work |

## 9. Key Takeaways

By completing this task, I strengthened my understanding of backend development using FastAPI, SQLAlchemy, and PostgreSQL.

My key takeaways were:

- Understanding how REST APIs work.
- Implementing CRUD operations for database records.
- Connecting a backend application to a database.
- Creating database models and understanding their purpose.
- Validating incoming requests using Pydantic.
- Testing APIs using Postman.
- Organizing code into reusable and maintainable modules.
- Understanding basic database relationships.
- Learning how a React frontend consumes backend APIs.
- Practicing Python dictionaries and hash-map concepts.
- Understanding how Git and GitHub help manage and share project code.

## 10. Challenges and Solutions



### Challenge : Database Integration

**Challenge:** Understanding how FastAPI, SQLAlchemy, and the database work together.

**Solution:** I reviewed the database engine, session management, models, and query execution process to understand the complete data flow.

### Challenge : API Validation

**Challenge:** Understanding how invalid or incomplete request data is handled.

**Solution:** I worked with request schemas and tested invalid payloads to understand how validation errors are generated.

### Challenge : Backend Code Organization

**Challenge:** Understanding how to separate application logic into different files.

**Solution:** I organized the code according to its responsibilities, including routes, models, schemas, database configuration, and CRUD functions.

## 11. Final Summary

I completed all assigned tasks related to FastAPI CRUD development and database integration. I created database models, developed CRUD APIs, connected the database, tested endpoints using Postman, handled API validation, and organized the backend modules.

I also practiced API design, database relationships, backend architecture, React API consumption concepts, Python CRUD logic, and hash-map implementation.

This task improved my practical understanding of how backend applications manage data, communicate through REST APIs, and maintain clean and organized code. It also helped me build a stronger foundation for developing full-stack applications using React, FastAPI, and PostgreSQL.

**Final Status: All assigned tasks and deliverables completed.**
