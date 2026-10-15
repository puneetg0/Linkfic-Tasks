# Day 19 – Docker, Containerization, Deployment & DSA

**Internship:** Python Full Stack Developer Internship
**Project:** CineShelf – Movie Collection Management Application
**Day:** 19
**Focus:** Docker, FastAPI Deployment, Environment Variables, React Production Build, and DSA

---

## 1. Objective

The objective of Day 19 is to understand how full-stack applications are prepared for deployment in a production environment.

During this task, I will learn Docker fundamentals, understand the difference between containers and virtual machines, create a basic Dockerfile for the FastAPI backend, explore deployment platforms, and understand environment variables and the React production build process.

I will also practice Kadane's Algorithm to improve problem-solving skills using Python.

---

## 2. Tasks Assigned

| # | Task | Status |
|---|---|---|
| 1 | Learn what Docker is and why it is used | ✅ Done |
| 2 | Understand Containers vs. Virtual Machines | ✅ Done |
| 3 | Create a basic Dockerfile for the FastAPI backend | ✅ Done |
| 4 | Learn the deployment workflow for a full-stack application | ✅ Done |
| 5 | Research free deployment platforms | ✅ Done |
| 6 | Understand environment variables and configuration management | ✅ Done |
| 7 | Learn the difference between development and production environments | ✅ Done |
| 8 | Understand the React production build process | ✅ Done |
| 9 | Practice Kadane's Algorithm and the Maximum Subarray problem | ✅ Done |

---

## 3. Topics Covered

### 3.1 What Is Docker?

Docker is a platform that allows developers to package an application and its dependencies into a container.

A container provides a consistent environment for running an application, helping reduce problems caused by differences between development and deployment environments.

For example, CineShelf uses React for the frontend and FastAPI for the backend. The backend also requires Python packages, configuration values, and a database connection.

Docker helps package the backend and its required dependencies so it can run consistently on different compatible systems.

**Why Docker is used:**
- Provides a consistent application environment
- Simplifies application setup
- Helps manage dependencies
- Supports application deployment
- Makes it easier to run isolated services
- Helps teams work with the same application configuration

> Think of it like a lunchbox. You pack everything you need inside.
> Wherever you take it, you have your exact meal — no surprises.

### 3.2 What Is a Container?

A container is an isolated environment in which an application runs with the dependencies and configuration it needs.

Containers share the host operating system's kernel, making them generally lighter than full virtual machines.

**Example:** A FastAPI container can include the Python runtime, installed packages, and backend application code.

### 3.3 Containers vs. Virtual Machines

| Feature | Containers | Virtual Machines |
|---|---|---|
| Operating system | Share the host kernel | Run a guest operating system |
| Resource usage | Generally lightweight | Generally require more resources |
| Startup | Usually fast | Usually slower |
| Isolation | Process-level isolation | Virtualized hardware and OS isolation |
| Common tools | Docker | VirtualBox, VMware |
| Typical use | Packaging and running applications | Running separate operating systems |

**Key learning:** Containers and virtual machines both provide isolation, but they work differently. Docker containers are especially useful for packaging and deploying applications consistently.

> A VM rents you an entire house. A container rents you one room.
> Same privacy, much lighter.

### 3.4 Important Docker Terms

| Term | Meaning |
|---|---|
| **Dockerfile** | A text file containing instructions for building an image |
| **Docker Image** | A packaged, read-only template used to create containers |
| **Docker Container** | A running or stopped instance of an image |
| **Docker Engine** | The software that builds and runs containers |
| **Docker Hub** | A registry where container images can be stored and shared |
| **Port Mapping** | Connects a port on the host machine to a port inside a container |
| **Volume** | Provides persistent or shared storage for container data |
| **Environment Variable** | A configuration value supplied to an application at runtime or build time |

The basic workflow is:

```
Dockerfile  →  Docker Image  →  Docker Container
```

---

## 4. Practical Task – Create a Dockerfile for FastAPI

### 4.1 What Is a Dockerfile?

A Dockerfile contains instructions Docker uses to build an image for an application.

For the CineShelf backend, the Dockerfile specifies the Python environment, installs dependencies, copies the backend code, and defines the command used to start FastAPI.

### 4.2 Backend Dockerfile

Create a file named `Dockerfile` inside the `backend/` directory.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 4.3 Explanation of Each Instruction

**1. `FROM python:3.12-slim`**

Selects a lightweight Python base image. Docker uses this as the starting environment for the backend.

**2. `WORKDIR /app`**

Sets `/app` as the working directory inside the image. Subsequent commands run from this directory unless otherwise specified.

**3. `COPY requirements.txt .`**

Copies the dependency list into the image. This allows Docker to install the required packages before copying the remaining application files.

**Why copy this first?** Docker saves each step as a cache layer. If you change a Python file, Docker skips re-installing dependencies because that step didn't change. This makes rebuilds much faster.

**4. `RUN pip install --no-cache-dir -r requirements.txt`**

Installs the Python dependencies listed in `requirements.txt`, such as FastAPI, Uvicorn, and SQLAlchemy.

**5. `COPY . .`**

Copies the backend project files into the container's working directory. A `.dockerignore` file should exclude unnecessary files such as `.venv`, `__pycache__`, and secret configuration files.

**6. `EXPOSE 8000`**

Documents the port the application is expected to use. It does not publish the port automatically.

**7. `CMD [...]`**

Defines the default command that starts the FastAPI application using Uvicorn. The host `0.0.0.0` allows the application to accept connections from outside the container.

### 4.4 Build and Run the Container (Step by Step)

Run these commands from the `backend/` directory.

**Step 1 — Install Docker Desktop**

Download from https://www.docker.com/products/docker-desktop and install it. Open Docker Desktop and confirm the whale icon appears in the taskbar before continuing.

**Step 2 — Build the image**

```bash
docker build -t cineshelf-backend .
```

This reads the `Dockerfile` and creates an image named `cineshelf-backend`. The first time will download the base image, which takes a minute or two.

**Step 3 — Run the container**

```bash
docker run --rm -p 8000:8000 cineshelf-backend
```

- `--rm` removes the container automatically when it stops
- `-p 8000:8000` maps port 8000 on your machine to port 8000 inside the container

**Step 4 — Test the application**

Open the following URL in a browser:

```
http://localhost:8000/docs
```

The FastAPI interactive API documentation should appear if the application starts successfully.

**Step 5 — Check what is running**

Open a second terminal while the container is running:

```bash
docker ps
```

You will see something like:

```
CONTAINER ID   IMAGE                STATUS        PORTS
a1b2c3d4e5f6   cineshelf-backend    Up 30 sec     0.0.0.0:8000->8000/tcp
```

The `->` shows port mapping. `0.0.0.0:8000->8000/tcp` means your machine's port 8000 is connected to the container's port 8000.

**Step 6 — Stop the container**

Press `Ctrl + C` in the terminal where the container is running, or run:

```bash
docker stop <container_id>
```

### 4.5 Running Both Services with Docker Compose

Docker Compose lets you run the backend and frontend together with one command.

```bash
docker compose up --build
```

| Service | URL |
|---|---|
| Frontend (React) | http://localhost:3000 |
| Backend (FastAPI) | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |

Stop everything:

```bash
docker compose down
```

### 4.6 Quick Docker Command Reference

| Command | What it does |
|---|---|
| `docker build -t name .` | Build an image from the current directory |
| `docker run -p 8000:8000 name` | Run a container with port mapping |
| `docker compose up --build` | Build images and start all services |
| `docker compose up` | Start all services using cached build |
| `docker compose down` | Stop and remove containers |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers including stopped |
| `docker images` | List all built images |
| `docker logs <container_id>` | View container output |
| `docker stop <container_id>` | Stop a running container |

### 4.7 Important Backend Considerations

Before deploying CineShelf, verify that:

- All required Python packages are listed in `requirements.txt`
- The application starts using the correct module path
- Secret keys and API credentials are not hardcoded
- The database connection is configured correctly
- CORS settings permit requests from the deployed frontend
- Production configuration does not expose debugging information

---

## 5. Environment Variables

### 5.1 What Are Environment Variables?

Environment variables are key-value pairs used to configure an application without hardcoding environment-specific values in source code.

For example, a database URL may be different on a developer's computer and on a production server. Instead of writing it directly into the code, the application reads it from an environment variable.

### 5.2 Example in Python

```python
import os

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL is not configured")
```

- `import os` imports Python's operating-system utilities
- `os.getenv("DATABASE_URL")` reads the environment variable
- The condition checks whether the value is missing
- The error makes the configuration problem clear instead of silently continuing

### 5.3 Common Environment Variables

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | Database connection string |
| `SECRET_KEY` | Secret used for signing or cryptographic operations |
| `FRONTEND_URL` | Deployed frontend origin for CORS |
| `PORT` | Port provided by some hosting platforms |
| `OPENAI_API_KEY` | API credential when using the OpenAI API |

### 5.4 Environment Variables in React (Vite)

In a Vite application, variables prefixed with `VITE_` can be accessed in frontend code:

```javascript
const apiUrl = import.meta.env.VITE_API_URL;
```

**Security rule:** Variables included in a frontend build are visible to users. Never put database passwords, private API keys, or backend secret keys in frontend environment variables. Keep private credentials on the backend.

### 5.5 What Is a `.env` File?

A `.env` file is a convenient way to store local configuration values.

```env
DATABASE_URL=postgresql+psycopg://user:password@localhost/cineshelf
SECRET_KEY=replace_with_a_local_development_secret
```

Do not commit real secrets to GitHub. Add `.env` files to `.gitignore` and configure secrets through the hosting platform's dashboard in production.

---

## 6. Development vs. Production

| Area | Development | Production |
|---|---|---|
| Purpose | Building and testing | Serving real users |
| Frontend | Development server (`npm run dev`) | Optimized static build (`npm run build`) |
| Backend | Local development server | Configured application server |
| Debugging | Detailed errors | Safe error responses and server-side logs |
| Configuration | Local `.env` file | Environment variables set in hosting dashboard |
| Database | Often local or temporary | Properly managed persistent database |
| Security | Development safeguards | Strong production security controls |

**Why this matters:** An application that works locally may fail after deployment because of missing dependencies, incorrect API URLs, unavailable databases, CORS restrictions, or missing environment variables. Production preparation helps identify these problems before users encounter them.

---

## 7. React Production Build

### 7.1 What Is a Production Build?

During development, React runs through a development server that supports rapid updates and debugging.

A production build generates optimized frontend assets that can be served to users by a static hosting platform or web server.

### 7.2 Build Commands

Run these commands from the `frontend/` directory:

```bash
npm install
npm run build
npm run preview
```

- `npm install` — installs the dependencies specified by the project
- `npm run build` — creates the production assets in the `dist/` directory
- `npm run preview` — serves the built assets locally so you can check the output before deploying

The `dist/` folder is what gets deployed. No Node.js is needed at runtime — it is just static files.

### 7.3 Deployment Requirements

Before deploying the frontend:

- Verify that the build completes without errors
- Configure the correct backend API URL (`VITE_API_URL`)
- Confirm that the deployed backend accepts frontend requests
- Configure client-side routing fallback on the hosting platform
- Check the browser console and network requests for errors

---

## 8. Full-Stack Deployment Workflow

For CineShelf, the React frontend and FastAPI backend are deployed as separate services.

```
You write code  →  git push  →  GitHub  →  Render detects push
                                                    │
                              ┌─────────────────────┴──────────────────────┐
                              ▼                                             ▼
                     Backend (FastAPI)                           Frontend (React)
                     Render runs Uvicorn                         Render builds dist/
                     Reads DATABASE_URL                          Reads VITE_API_URL
                     from environment vars                       at build time
                              │
                              ▼
                    PostgreSQL (hosted database)
```

### Deployment Steps

1. **Prepare the code** — check dependencies, configuration, API endpoints, and startup commands
2. **Test locally** — verify registration, login, movie CRUD, search, and protected routes
3. **Prepare the backend** — create the Dockerfile and configure environment variables
4. **Deploy the backend** — publish the FastAPI service to a hosting platform
5. **Configure the database** — use a persistent hosted database
6. **Deploy the frontend** — build React and publish the generated assets
7. **Connect frontend and backend** — configure `VITE_API_URL` and backend CORS settings
8. **Test the live application** — verify API responses, authentication, and database persistence
9. **Monitor the application** — review logs, errors, and resource usage

### CineShelf — Live

- **Frontend:** https://cineshelf-frontend-5qiq.onrender.com
- **Backend:** Render (FastAPI + Uvicorn)
- **Database:** PostgreSQL (hosted)

---

## 9. Research – Free Deployment Platforms

The availability and limits of free hosting plans can change. Review current pricing, resource limits, and service policies before selecting a platform.

| Component | Platforms | What to Check |
|---|---|---|
| React frontend | Vercel, Netlify, Cloudflare Pages | Build settings, static hosting, custom domains |
| FastAPI backend | Render, Railway, Koyeb, Fly.io | Python/Docker support, free-tier eligibility, sleep limits |
| PostgreSQL database | Supabase, Neon | Storage, connection limits, free-plan restrictions |

**Notes:**
- Render free tier spins down after 15 minutes of inactivity (cold starts ~30 seconds)
- Neon offers a free PostgreSQL database with no 90-day expiry, unlike Render's database free tier
- Vercel is excellent for React frontends but does not host persistent backends

### Deployment Checklist

- [ ] Confirm the platform supports the selected framework
- [ ] Check whether a free plan is currently available
- [ ] Configure environment variables in the hosting dashboard
- [ ] Configure the database and persistence
- [ ] Set the frontend's `VITE_API_URL`
- [ ] Configure backend CORS to allow the frontend domain
- [ ] Verify the deployed API and frontend
- [ ] Review service logs and resource limits

---

## 10. Project Structure

```
Day19/
├── backend/
│   ├── Dockerfile          ← Instructions to build the FastAPI image
│   └── .dockerignore       ← Files excluded from the Docker image
├── frontend/
│   ├── Dockerfile          ← Multi-stage build: Node builds → Nginx serves
│   └── nginx.conf          ← Nginx config for React SPA routing
├── docker-compose.yml      ← Runs backend + frontend together locally
├── deployment_notes.md     ← Full research notes
├── dsapractice.py          ← Kadane's Algorithm implementation
└── README.md               ← This file
```

---

## 11. DSA Practice – Kadane's Algorithm

### 11.1 Problem: Maximum Subarray

Given an array of integers, find the largest possible sum of a contiguous, non-empty subarray.

**Example:**

```
Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Reason: The subarray [4, -1, 2, 1] has the largest sum → 4 + (-1) + 2 + 1 = 6
```

### 11.2 Python Implementation

```python
def max_subarray(numbers):
    current_sum = numbers[0]
    max_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(numbers))  # Output: 6
```

### 11.3 Explanation

**Step 1 — Initialize the sums**

```python
current_sum = numbers[0]
max_sum = numbers[0]
```

`current_sum` stores the best sum of a subarray ending at the current position.
`max_sum` stores the largest sum found so far.

Initializing both with the first element ensures the algorithm handles arrays with only negative numbers.

**Step 2 — Iterate through the remaining elements**

```python
for number in numbers[1:]:
```

The loop begins with the second element because the first was used for initialization.

**Step 3 — Decide whether to extend or restart the subarray**

```python
current_sum = max(number, current_sum + number)
```

Two possibilities at each step:
- Start a new subarray at the current number
- Extend the existing subarray by adding the current number

Whichever gives the larger value is chosen.

**Step 4 — Update the maximum sum**

```python
max_sum = max(max_sum, current_sum)
```

If the current subarray beats the previous best, update the answer.

**Step 5 — Return the result**

```python
return max_sum
```

### 11.4 Complexity

- **Time complexity:** O(n) — each element is processed once
- **Space complexity:** O(1) — only two variables are used regardless of input size

### 11.5 Test Cases

| Input | Expected Output |
|---|---:|
| `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` | `6` |
| `[1, 2, 3, 4]` | `10` |
| `[-5, -2, -8]` | `-2` |
| `[5]` | `5` |
| `[-1, 2, 3, -2, 4]` | `7` |

Run the practice file:

```bash
python dsapractice.py
```

Expected: all tests pass ✓

---

## 12. Work Completed / Deliverables

- [x] Understand Docker images and containers
- [x] Explain containers vs. virtual machines
- [x] Create a basic FastAPI Dockerfile
- [x] Build and run the Docker image locally
- [x] Verify the backend through `/docs`
- [x] Review environment-variable configuration
- [x] Generate and test the React production build
- [x] Research deployment platform requirements
- [x] Practice Kadane's Algorithm
- [ ] Update the project documentation and GitHub repository

---

## 13. Challenges to Investigate

During this task, I will investigate common problems that occur when preparing an application for deployment:

- Missing Python dependencies
- Incorrect FastAPI application entry points
- Docker build failures
- Incorrect port configuration
- Missing environment variables
- Incorrect frontend API URLs
- CORS errors between frontend and backend
- Database connection or persistence problems
- React production build errors

For each problem, identify the cause, apply a fix, and verify that the application works correctly.

---

## 14. Key Learnings

By completing this task, I understand:

- How Docker packages an application and its dependencies
- How Dockerfiles, images, and containers work together
- Why environment variables are important for configuration
- How development environments differ from production environments
- How to prepare a React application for production
- How frontend, backend, and database services communicate after deployment
- How to solve the Maximum Subarray problem efficiently using Kadane's Algorithm

---

## 15. Git Commands

Run these commands from the repository root after reviewing the changes:

```bash
git status
git add Day19/README.md Day19/backend/Dockerfile
git commit -m "docs: document Docker and deployment learning for Day 19"
git push
```

Adjust the paths to match the actual files created. Include the Dockerfile only after it has been reviewed.

---

## 16. Final Outcome

Day 19 focuses on preparing CineShelf for deployment by learning containerization, backend configuration, and frontend production builds. It also develops an understanding of deployment architecture and reinforces algorithmic problem-solving through Kadane's Algorithm.

The final goal is to be able to explain the deployment workflow, demonstrate a locally running FastAPI Docker container, and describe the steps needed to make the full-stack application accessible online.
