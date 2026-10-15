# ─────────────────────────────────────────────
#  CineShelf – Backend Dockerfile
#  Base image: official Python slim image
# ─────────────────────────────────────────────

# 1. Choose a lightweight base image
FROM python:3.12-slim

# 2. Set a working directory inside the container
WORKDIR /app

# 3. Copy dependency list first (Docker layer-cache trick —
#    dependencies only re-install when requirements.txt changes)
COPY requirements.txt .

# 4. Install Python dependencies
#    --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application source code
COPY . .

# 6. Expose the port Uvicorn will listen on
EXPOSE 8000

# 7. Start the FastAPI app with Uvicorn
#    --host 0.0.0.0 makes it reachable from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
