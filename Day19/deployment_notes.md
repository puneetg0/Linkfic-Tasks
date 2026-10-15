# Day 19 — Deployment Research Notes

## What is Docker?

Docker packages your app and everything it needs (Python, libraries, config)
into a single portable unit called a **container**. You ship the container,
not just the code — so "it works on my machine" stops being an excuse.

### Key terms

| Term | What it means |
|---|---|
| **Image** | A read-only blueprint (built from a Dockerfile) |
| **Container** | A running instance of an image |
| **Dockerfile** | Instructions to build an image |
| **Docker Hub** | Public registry for sharing images |
| **Docker Compose** | Tool for running multi-container apps locally |

---

## Containers vs Virtual Machines

| | Container | Virtual Machine |
|---|---|---|
| **Size** | MBs | GBs |
| **Boot time** | Seconds | Minutes |
| **Isolation** | Process-level (shares OS kernel) | Full OS |
| **Use case** | Microservices, apps | Full system emulation |
| **Example** | Docker | VirtualBox, VMware |

**Analogy:** A VM is like renting an entire house. A container is like renting
one room in a shared house — lighter, faster, but still private.

---

## Deployment Workflow (CineShelf)

```
Local Development
      │
      ▼
  git push  ──────────────────────────────────────►  GitHub
                                                          │
                                              Auto-deploy trigger
                                                          │
                              ┌───────────────────────────┴──────────────────────┐
                              ▼                                                   ▼
                     Render (Backend)                               Render (Frontend)
                   FastAPI + Uvicorn                               Static site / Nginx
                   Reads DATABASE_URL                             Reads VITE_API_URL
                   from environment                               at build time
                              │
                              ▼
                    PostgreSQL (Render DB
                     or Supabase/Neon)
```

### Steps when deploying a change

1. Make changes locally and test them
2. `git add` → `git commit` → `git push origin main`
3. Render detects the push and re-deploys automatically
4. Backend: Render runs `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Frontend: Render runs `npm run build` and serves the `dist/` folder

---

## Environment Variables

Environment variables are how you pass **secrets and config** without
hardcoding them into your source code.

### Why they matter

- Passwords, API keys, and DB URLs must never be in your repo
- The same image can run in dev vs prod by changing env vars only
- Render, Railway, Fly.io — all have a UI to set them per service

### CineShelf env vars

**Backend**
```
DATABASE_URL=postgresql+psycopg://user:password@host/dbname
SECRET_KEY=your-random-secret-key-here
```

**Frontend (Vite)**
```
VITE_API_URL=https://your-backend.onrender.com
```

> Vite only embeds env vars that start with `VITE_` into the build.
> They are baked in at **build time**, not runtime.

### Production vs Development

| | Development | Production |
|---|---|---|
| **Database** | Local PostgreSQL | Hosted (Render, Supabase, Neon) |
| **API URL** | `http://localhost:8000` | `https://cineshelf-api.onrender.com` |
| **Debug mode** | On | Off |
| **CORS** | Allows localhost | Allows only your real domain |
| **Secrets** | `.env` file (gitignored) | Env vars set in hosting dashboard |

---

## Free Deployment Platforms (Research)

### Render (Currently using ✓)

- **Free tier:** Yes — spins down after 15 min inactivity (cold starts ~30s)
- **Best for:** Full-stack apps, FastAPI backends, static React sites
- **Database:** Managed PostgreSQL (free tier: 1 GB, expires after 90 days)
- **Auto-deploy:** Yes, from GitHub
- **URL:** https://render.com

### Railway

- **Free tier:** $5 free credit/month (hobby plan)
- **Best for:** Small backends, databases
- **Database:** PostgreSQL included
- **Auto-deploy:** Yes, from GitHub
- **URL:** https://railway.app

### Fly.io

- **Free tier:** 3 shared-CPU VMs, 3 GB storage
- **Best for:** Dockerized apps — you deploy a Dockerfile directly
- **Database:** Postgres add-on
- **Auto-deploy:** Via CLI (`flyctl deploy`)
- **URL:** https://fly.io

### Vercel (Frontend only)

- **Free tier:** Generous — unlimited static deploys
- **Best for:** React/Vite frontends only (no persistent backend)
- **Auto-deploy:** Yes, from GitHub
- **URL:** https://vercel.com

### Supabase / Neon (Database only)

- **Free tier:** Both offer free PostgreSQL
- **Best for:** Replacing the Render DB (no 90-day expiry on Neon)
- **URL:** https://supabase.com | https://neon.tech

### Comparison for CineShelf

| Platform | Frontend | Backend | Database | Free |
|---|---|---|---|---|
| **Render** | ✓ | ✓ | ✓ (90 days) | ✓ |
| **Railway** | ✗ | ✓ | ✓ | Limited |
| **Fly.io** | ✗ | ✓ | ✓ | ✓ |
| **Vercel** | ✓ | ✗ | ✗ | ✓ |
| **Neon** | ✗ | ✗ | ✓ (no expiry) | ✓ |

**Recommendation:** Keep Render for backend + frontend. Switch the DB to
**Neon** to avoid the 90-day free-tier expiry on Render's PostgreSQL.

---

## Build Process (Frontend)

```bash
npm run build
```

What happens:
1. Vite reads `vite.config.js`
2. Bundles all JSX/JS/CSS into optimised static files
3. Outputs to `dist/` folder
4. `dist/` is what gets deployed (no Node.js needed at runtime)

The `dist/` folder should be gitignored — it's generated, not source code.

---

## Dockerfile Concepts Learned Today

```dockerfile
FROM python:3.12-slim        # Base image (OS + Python pre-installed)
WORKDIR /app                 # All commands run from here inside the container
COPY requirements.txt .      # Copy just this first (layer caching)
RUN pip install ...          # Runs during image BUILD
COPY . .                     # Copy app source
EXPOSE 8000                  # Documents which port the app uses
CMD ["uvicorn", ...]         # Runs when the CONTAINER STARTS
```

### Layer caching trick

Docker caches each instruction as a "layer". If a layer hasn't changed,
Docker skips rebuilding it. By copying `requirements.txt` before `COPY . .`,
dependencies are only re-installed when `requirements.txt` actually changes —
not every time you edit a Python file. This makes rebuilds much faster.

---

## YouTube Resources

- **TechWorld with Nana** — Docker for Beginners (full course)
- **Traversy Media** — Deploy FastAPI to Render
- **freeCodeCamp** — Docker + Docker Compose crash course

Search terms used:
- "Docker for Beginners"
- "FastAPI Docker deployment"
- "Deploy React FastAPI Application Render"
