# ─────────────────────────────────────────────
#  CineShelf – Frontend Dockerfile  (multi-stage)
# ─────────────────────────────────────────────

# ── Stage 1: Build ──────────────────────────
# Use Node to install deps and run `vite build`
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files first (layer-cache trick)
COPY package*.json ./

# Install all dependencies (including devDeps needed to build)
RUN npm ci

# Copy source code
COPY . .

# Build the production bundle → /app/dist
RUN npm run build

# ── Stage 2: Serve ──────────────────────────
# Use a tiny Nginx image to serve the static files
FROM nginx:alpine

# Remove default Nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy the built React app from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Nginx config for Single-Page App routing
# (redirects 404s back to index.html so React Router handles them)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
