# Day 23: Full-Stack Project Setup and JWT Authentication

## 1. Tasks Assigned

1. Create the React application.
2. Create the FastAPI application.
3. Configure the database.
4. Implement Login and Registration.
5. Configure JWT Authentication (Token Issuing and Verification).
6. Create the project folder structure.
7. Set up environment variables.

---

## 2. Project Overview

The objective of this task is to initialize the Blood Donation Management System as a full-stack web application using React, FastAPI, and PostgreSQL.

The project establishes communication between the frontend and backend, configures database connectivity, and implements user registration, login, password hashing, and JWT-based authentication.

The application is organized into separate modules to improve maintainability, readability, security, and scalability. This foundation will support future features such as donor profile management, blood group search, blood requests, and donation tracking.

## 3. Technologies Used

- **React:** Frontend user interface development.
- **Vite:** React project initialization and development server.
- **Python:** Backend programming language.
- **FastAPI:** REST API development and request handling.
- **PostgreSQL:** Relational database management.
- **SQLAlchemy:** Object-Relational Mapping (ORM).
- **Pydantic:** Request validation and response schemas.
- **JWT:** Token-based authentication.
- **Argon2:** Secure password hashing.
- **Axios:** Frontend-to-backend API communication.
- **Python-dotenv:** Environment variable management.
- **Git and GitHub:** Version control and project hosting.

---

## 4. Task 1: Create the React Application

### Objective

Initialize the frontend application using React to provide an interactive user interface for the Blood Donation Management System.

### Brief About the Topic

React is a JavaScript library used to build component-based user interfaces. In this project, it handles user registration, login forms, navigation, validation messages, and API responses.

Vite provides a development environment for running and building the React application. React Router is used to navigate between pages, and Axios sends HTTP requests to the FastAPI backend.

### Implementation Steps

1. Initialize the React application using Vite.
2. Install the required dependencies.
3. Create the main application component.
4. Create login and registration pages.
5. Configure React Router for navigation.
6. Create reusable components where required.
7. Configure Axios for backend communication.
8. Handle API responses and error messages.
9. Run the frontend development server.
10. Verify that the application loads correctly.

### Commands

```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm install axios react-router-dom
npm run dev
```

### Expected Outcome

A working React application with login and registration pages, navigation, and the foundation for communication with the backend.

### Learning Outcomes

- Understanding React project initialization.
- Working with components and JSX.
- Understanding client-side routing.
- Handling form input and state.
- Connecting the frontend to REST APIs.

---

## 5. Task 2: Create the FastAPI Application

### Objective

Initialize the backend application using FastAPI to handle authentication requests, validate input, execute database operations, and return API responses.

### Brief About the Topic

FastAPI is a Python web framework used to build REST APIs. It supports request validation, dependency injection, automatic documentation, and authentication integrations.

The backend processes registration and login requests, interacts with PostgreSQL, issues JWT access tokens, and provides protected endpoints for authenticated users.

### Implementation Steps

1. Create the backend directory.
2. Create a Python virtual environment.
3. Activate the virtual environment.
4. Install FastAPI, Uvicorn, and required libraries.
5. Create the main application file.
6. Configure CORS for the React development server.
7. Create modules for routes, models, schemas, and authentication.
8. Define the required API endpoints.
9. Start the FastAPI development server.
10. Test endpoints using Swagger UI.

### Commands

```bash
mkdir backend
cd backend

python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy psycopg2-binary python-dotenv "pwdlib[argon2]" PyJWT email-validator
pip freeze > requirements.txt
```

Run the application from the backend directory:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

`http://127.0.0.1:8000/docs`

### Expected Outcome

A working FastAPI backend with organized modules, API routes, request validation, and interactive API documentation.

### Learning Outcomes

- Understanding backend application initialization.
- Developing REST APIs.
- Working with Python virtual environments.
- Understanding CORS and HTTP requests.
- Organizing backend logic into separate modules.
- Testing APIs using Swagger UI.

---

## 6. Task 3: Configure the Database

### Objective

Configure PostgreSQL and connect it to FastAPI using SQLAlchemy to store user accounts and application information.

### Brief About the Topic

PostgreSQL is a relational database management system that stores structured information in tables. SQLAlchemy provides an ORM that allows Python applications to interact with database records using models and queries.

The initial database will contain user information, including a unique identifier, name, email address, and hashed password. Additional tables can be created later for donors, blood requests, and donations.

### Implementation Steps

1. Install and configure PostgreSQL.
2. Create the project database.
3. Configure the database connection URL.
4. Initialize the SQLAlchemy engine.
5. Configure database sessions.
6. Create a base class for database models.
7. Define the user model.
8. Initialize the database tables.
9. Verify database connectivity.
10. Handle database errors and duplicate email addresses.

### SQL Command

```sql
CREATE DATABASE blood_donation_db;
```

### Database Configuration

Create `backend/app/database.py`:

```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Initial User Table

| Column | Purpose |
|---|---|
| `id` | Unique user identifier |
| `name` | User's name |
| `email` | Unique email address |
| `hashed_password` | Stored password hash |

### Expected Outcome

A PostgreSQL database connected to FastAPI, with a user model available for registration and login.

### Learning Outcomes

- Understanding relational database concepts.
- Working with PostgreSQL and SQL.
- Creating database models using SQLAlchemy.
- Managing database sessions.
- Understanding primary keys and unique constraints.
- Separating database configuration from application logic.

---

## 7. Task 4: Implement Login and Registration

### Objective

Develop registration and login functionality so users can create accounts and authenticate themselves before accessing protected application features.

### Brief About the Topic

Registration allows new users to create accounts, while login verifies the identity of existing users.

Registration involves validating user information, checking for duplicate accounts, hashing passwords, and saving user records. Login involves retrieving the user record and verifying the submitted password against the stored password hash.

### Registration Workflow

1. The user opens the registration page.
2. The user enters their name, email, and password.
3. React sends the registration request to FastAPI.
4. FastAPI validates the incoming data using Pydantic.
5. The backend checks whether the email already exists.
6. The password is hashed using Argon2.
7. The user record is saved in PostgreSQL.
8. The API returns a success response.

### Login Workflow

1. The user enters their email and password.
2. React sends a login request to FastAPI.
3. The backend retrieves the user record by email.
4. The submitted password is verified against the stored hash.
5. Invalid credentials are rejected.
6. Valid credentials allow the backend to issue a JWT access token.
7. The frontend uses the token to request protected resources.

### API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate an existing user |
| GET | `/auth/me` | Retrieve the authenticated user's profile |

### Validation Requirements

- Name must meet the minimum length requirement.
- Email must have a valid format.
- Password must meet the minimum length requirement.
- Duplicate email addresses must be rejected.
- Passwords must be hashed before storage.
- Invalid login attempts must return an authentication error.
- Passwords and other sensitive values must not appear in API responses.

### Expected Outcome

Users can register accounts, log in with valid credentials, and receive appropriate responses for invalid inputs or authentication failures.

### Learning Outcomes

- Understanding authentication workflows.
- Implementing frontend forms.
- Validating data with Pydantic.
- Performing database queries.
- Hashing and verifying passwords.
- Handling API responses and errors.

---

## 8. Task 5: Configure JWT Authentication

### Objective

Implement JWT-based authentication to issue access tokens after successful login and verify tokens when users request protected resources.

### Brief About the Topic

JSON Web Token (JWT) is a compact token format used to transmit signed claims between a client and server.

After successful authentication, FastAPI generates a signed access token containing the user's identifier and an expiration time. The frontend sends this token in the HTTP Authorization header when accessing protected endpoints.

JWT signatures help the backend detect token modification. Token expiry limits how long an access token remains valid.

### Token Issuing Process

1. Verify the user's email and password.
2. Create a token payload containing the user's identifier.
3. Add an expiration timestamp.
4. Sign the token using a secret key and an approved algorithm.
5. Return the token to the frontend.
6. Configure an appropriate token lifetime.

### Token Verification Process

1. Receive the access token from the request.
2. Extract the token from the bearer authorization header.
3. Verify the token signature.
4. Validate the expiration time.
5. Extract the user identifier from the token.
6. Retrieve the corresponding user record.
7. Allow access only when authentication succeeds.
8. Return HTTP 401 for missing, invalid, or expired tokens.

### Authorization Header Example

```http
Authorization: Bearer <access_token>
```

### Security Considerations

- Use a strong, randomly generated JWT secret.
- Never include passwords or confidential data in JWT payloads.
- Verify signatures and expiration times.
- Keep the signing secret out of source code.
- Use HTTPS in production.
- Protect sensitive endpoints with authentication dependencies.
- Avoid placing access tokens in browser local storage without evaluating the security risks.
- Consider secure session cookies or another carefully designed token-storage strategy for production.

A JWT is signed by default, not encrypted. Its payload should not contain sensitive information.

### Expected Outcome

The backend issues access tokens after successful login and validates them before allowing access to protected API endpoints.

### Learning Outcomes

- Understanding JWT structure and claims.
- Implementing token generation and verification.
- Understanding authentication and authorization.
- Working with bearer tokens.
- Handling expired and invalid tokens.
- Applying secure authentication practices.

---

## 9. Password Hashing Concepts

### 9.1 Introduction

Password hashing is a security technique that transforms a password into a derived hash before it is stored in a database. It helps protect user credentials if the database is exposed.

In the Blood Donation Management System, password hashing is used during registration, while password verification is performed during login.

A suitable password-hashing algorithm is deliberately computationally expensive, making large-scale password guessing more difficult.

### 9.2 Why Password Hashing Is Important

- Prevents passwords from being stored in plaintext.
- Reduces the risk of exposing original passwords in a database leak.
- Supports secure user authentication.
- Makes offline password guessing more expensive.
- Helps protect user credentials.

Hashing does not guarantee that a password can never be guessed. Strong passwords and appropriate hashing parameters remain important.

### 9.3 How Password Hashing Works

**During Registration:**

1. The user enters a password.
2. The backend receives the password over a secure connection.
3. The password-hashing library generates a unique salt and derives a password hash.
4. The resulting hash is stored in PostgreSQL.
5. The original password is not stored.

**During Login:**

1. The user enters their email and password.
2. The backend retrieves the stored password hash.
3. The password verification function checks the submitted password against the stored hash.
4. If verification succeeds, authentication continues.
5. If verification fails, the backend rejects the login attempt.

A salt is a unique random value used in password hashing. It prevents identical passwords from automatically producing identical stored hashes when properly implemented.

### 9.4 Password Hashing Example Using Argon2

```python
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

# Registration
password = "ExamplePassword123!"
hashed_password = password_hash.hash(password)

# Login verification
is_valid = password_hash.verify(
    "ExamplePassword123!",
    hashed_password
)

print(is_valid)  # True
```

The example password is for demonstration only. The hash contains the information needed by the library to verify the password, including the salt and hashing parameters.

### 9.5 Hashing vs Encryption

| Password Hashing | Encryption |
|---|---|
| Designed to be one-way | Designed to be reversible with the appropriate key |
| Used for password storage | Used when data must later be recovered |
| Verification compares a candidate password with a stored hash | Decryption recovers the original data |
| Example: Argon2id | Example: AES |

### 9.6 Password Security Best Practices

- Use a dedicated password-hashing algorithm such as Argon2id.
- Never store plaintext passwords.
- Do not use ordinary SHA-256 or MD5 alone for password storage.
- Use unique salts, managed by a suitable password-hashing library.
- Verify passwords through the library's verification function.
- Apply reasonable password-length requirements.
- Use HTTPS to protect credentials in transit.
- Never log passwords or return them in API responses.
- Use generic login failure messages.

### 9.7 Application in the Project

Password hashing is implemented in the FastAPI authentication module.

During registration, the backend hashes the password before storing it in PostgreSQL. During login, the backend verifies the submitted password against the stored hash before issuing a JWT access token.

### 9.8 Learning Outcomes

- Understood the purpose of password hashing.
- Learned the difference between hashing and encryption.
- Practiced password hashing and verification with Argon2.
- Understood how password security supports registration and login.
- Learned secure credential-storage practices for backend applications.

---

## 10. Task 6: Create the Project Folder Structure

### Objective

Organize the frontend and backend into separate modules to improve readability, maintainability, scalability, and development efficiency.

### Brief About the Topic

A structured project separates user interface components, API communication, database operations, authentication logic, validation schemas, and route definitions.

This separation reduces code duplication, makes debugging easier, and supports future feature development.

### Proposed Folder Structure

```text
blood-donation-system/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   └── Register.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── .env
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   └── auth_routes.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── auth.py
│   ├── .env
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

### Folder Responsibilities

- `frontend/src/pages/`: Contains login and registration pages.
- `frontend/src/components/`: Contains reusable UI components.
- `frontend/src/services/`: Contains API communication logic.
- `backend/app/main.py`: Initializes FastAPI and registers routes.
- `backend/app/routes/`: Contains API endpoint definitions.
- `backend/app/database.py`: Configures database connections and sessions.
- `backend/app/models.py`: Defines database tables.
- `backend/app/schemas.py`: Validates request and response data.
- `backend/app/auth.py`: Contains password hashing and JWT utilities.
- `.env`: Stores environment-specific configuration.
- `requirements.txt`: Lists Python dependencies.
- `.gitignore`: Excludes sensitive and generated files from version control.

### Implementation Steps

1. Create separate frontend and backend directories.
2. Organize React pages and reusable components.
3. Create a service module for API requests.
4. Separate FastAPI routes from other application logic.
5. Create dedicated modules for database configuration and models.
6. Separate validation schemas from database models.
7. Keep authentication utilities in a dedicated module.
8. Maintain dependency and configuration files.
9. Add environment files and generated artifacts to `.gitignore`.

### Expected Outcome

A clean, modular project structure that supports the addition of donor management, blood group search, blood requests, and administrator functionality.

### Learning Outcomes

- Understanding modular application architecture.
- Applying separation of concerns.
- Improving code readability and maintainability.
- Organizing full-stack applications for collaboration.
- Preparing for future feature development.

---

## 11. Task 7: Set Up Environment Variables

### Objective

Configure environment variables to manage database credentials, JWT signing secrets, token expiry settings, and the frontend API URL outside the main source code.

### Brief About the Topic

Environment variables separate configuration from application logic. They allow different settings to be used for local development, testing, and production without modifying application source code.

The backend uses environment variables for database connectivity and JWT configuration. The React application uses a public API base URL to communicate with FastAPI.

### Backend Environment Configuration

Create `backend/.env`:

```dotenv
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@localhost:5432/blood_donation_db
JWT_SECRET_KEY=YOUR_GENERATED_RANDOM_SECRET
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace the placeholders with the appropriate local configuration.

### Frontend Environment Configuration

Create `frontend/.env`:

```dotenv
VITE_API_URL=http://127.0.0.1:8000
```

### Implementation Steps

1. Create the backend and frontend environment files.
2. Add the database connection URL.
3. Generate a secure random JWT signing secret.
4. Load backend configuration using `python-dotenv`.
5. Read configuration values through environment variables.
6. Configure the frontend API base URL.
7. Add actual `.env` files to `.gitignore`.
8. Restart development servers after changing environment values.
9. Verify that the application reads its configuration correctly.
10. Provide an `.env.example` file with placeholder values for other developers.

### Generating a Secure JWT Secret

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Copy the generated value into `JWT_SECRET_KEY` in the backend environment file.

### Security Considerations

- Never commit real database credentials or JWT signing secrets.
- Never expose backend secrets through frontend variables.
- Variables prefixed with `VITE_` are exposed to browser-side code.
- Use separate secrets and configuration for production.
- Avoid printing secrets in application logs.
- Restrict access to production environment configuration.

### Expected Outcome

The application reads its configuration from environment variables, keeps secrets out of source code, and supports different development environments.

### Learning Outcomes

- Understanding environment variables.
- Separating configuration from application logic.
- Managing database connection settings.
- Protecting authentication secrets.
- Improving application portability and deployment readiness.

---

## 12. Authentication Flow

The authentication flow connects the React frontend, FastAPI backend, password verification logic, and PostgreSQL database.

### Registration Flow

1. The user submits the registration form in React.
2. FastAPI validates the submitted information.
3. The backend checks whether the email is already registered.
4. The password is hashed.
5. The user record is saved in PostgreSQL.
6. The backend returns a success response.

### Login Flow

1. The user submits the login form.
2. FastAPI retrieves the user record.
3. The password is verified against the stored hash.
4. If the credentials are valid, the backend generates a JWT.
5. The frontend receives the access token.
6. The frontend sends the token when accessing a protected endpoint.
7. FastAPI verifies the token and retrieves the authenticated user's profile.

### Authentication Security

Authentication verifies the user's identity, while authorization determines what an authenticated user is permitted to do. Future versions can introduce role-based authorization for donors and administrators.

---

## 13. Testing and Validation

After implementing the assigned tasks, test the application using Swagger UI and the React frontend.

| Test Scenario | Expected Result |
|---|---|
| Register with valid details | Account created successfully |
| Register with duplicate email | Request rejected |
| Register with invalid email | Validation error |
| Login with valid credentials | JWT access token issued |
| Login with incorrect credentials | HTTP 401 |
| Access profile with a valid token | User profile returned |
| Access profile without a token | HTTP 401 |
| Access profile with an invalid token | HTTP 401 |
| Access profile with an expired token | HTTP 401 |
| Connect to PostgreSQL | Database connection succeeds |
| Load React application | Frontend starts successfully |

### Testing Tools

- FastAPI Swagger UI: `http://127.0.0.1:8000/docs`
- React development server: `http://localhost:5173`
- PostgreSQL and pgAdmin for database verification.
- Git for tracking source-code changes.

Testing should cover both successful requests and expected failure scenarios.

---

## 14. Challenges Faced

Potential challenges during implementation include:

- Setting up separate frontend and backend environments.
- Configuring PostgreSQL and SQLAlchemy.
- Organizing backend modules and dependencies.
- Implementing password hashing and verification.
- Generating and validating JWT access tokens.
- Resolving CORS and API connectivity issues.
- Managing environment variables securely.
- Handling duplicate email addresses and invalid credentials.
- Testing invalid and expired tokens.

Update this section with the actual problems encountered and the solutions implemented during development.

---

## 15. Learning Outcomes

After completing Day 23, the key learning outcomes include:

- Initialized a full-stack application using React and FastAPI.
- Configured PostgreSQL database connectivity.
- Organized the application into maintainable modules.
- Implemented user registration and login workflows.
- Applied password hashing and verification.
- Understood JWT token issuance and verification.
- Learned the difference between authentication and authorization.
- Configured environment variables securely.
- Tested authentication endpoints using Swagger UI.
- Practiced Git version control and GitHub repository management.

---


---

## 17. GitHub Repository

**Repository Name:** Blood Donation 

**Repository URL:** Add your GitHub repository link here.

**Suggested Commit Message:**

```text
Day 23: Initialize full-stack project and implement JWT authentication
```

### Git Commands

```bash
git add .
git commit -m "Day 23: Initialize project and JWT authentication"
git push origin main
```

Ensure that actual `.env` files, virtual environments, dependency caches, and other sensitive or generated files are excluded from the repository.

---

## 18. Task Completion Status

**Task Name:** Full-Stack Project Setup and JWT Authentication

**Day:** 23

**Status:** In Progress / Completed



**Final Summary:** Day 23 focuses on establishing the technical foundation of the Blood Donation Management System by initializing the frontend and backend, configuring the database, implementing secure authentication, organizing the project, and preparing the repository for future development.
