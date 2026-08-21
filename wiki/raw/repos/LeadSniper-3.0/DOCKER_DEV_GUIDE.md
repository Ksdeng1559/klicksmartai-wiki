# LeadSniper 3.0 - Docker Development Guide

Quick guide for running LeadSniper locally with Docker and hot-reload.

## 🚀 Quick Start

```bash
cd LeadSniper-3.0
docker-compose -f docker-compose.dev.yml up --build
```

**Access Points:**
- **Frontend**: http://localhost:5173 (Vite dev server with hot-reload)
- **Backend API**: http://localhost:8000
- **Backend Health**: http://localhost:8000/health
- **Backend Docs**: http://localhost:8000/docs (Swagger UI)

## ⚙️ Environment Setup

1. **Copy environment file** (if not already done):
   ```bash
   cp .env.local .env
   ```

2. **Required variables in `.env.local`**:
   ```env
   GEMINI_API_KEY=your-gemini-api-key
   APIFY_API_KEY=your-apify-api-key

   # Optional - for Supabase features
   SUPABASE_URL=your-supabase-url
   SUPABASE_KEY=your-supabase-key
   ```

## 📋 Common Commands

### Start Development Environment
```bash
# Start with logs
docker-compose -f docker-compose.dev.yml up

# Start in background
docker-compose -f docker-compose.dev.yml up -d

# Rebuild after dependency changes
docker-compose -f docker-compose.dev.yml up --build
```

### View Logs
```bash
# All services
docker-compose -f docker-compose.dev.yml logs -f

# Frontend only
docker-compose -f docker-compose.dev.yml logs -f frontend

# Backend only
docker-compose -f docker-compose.dev.yml logs -f backend
```

### Stop Services
```bash
# Stop gracefully
docker-compose -f docker-compose.dev.yml down

# Stop and remove volumes
docker-compose -f docker-compose.dev.yml down -v
```

### Restart Individual Service
```bash
# Restart frontend
docker-compose -f docker-compose.dev.yml restart frontend

# Restart backend
docker-compose -f docker-compose.dev.yml restart backend
```

## 🔥 Hot Reload Features

### Frontend (Vite)
- **Instant HMR**: Changes to `.tsx`, `.ts`, `.css` files reload automatically
- **State Preservation**: React Fast Refresh maintains component state
- **Volume Mount**: Code changes reflect immediately without rebuild

### Backend (FastAPI)
- **Auto-reload**: Python file changes trigger automatic server restart
- **Fast Iteration**: Uvicorn reloads in ~1-2 seconds
- **API Docs**: Swagger UI updates automatically at `/docs`

## 🐛 Debugging

### Enter Container Shell
```bash
# Frontend container
docker exec -it leadsniper-frontend-dev sh

# Backend container
docker exec -it leadsniper-backend-dev bash
```

### View Real-time Logs
```bash
# Combined logs
docker-compose -f docker-compose.dev.yml logs -f

# Filter by service
docker-compose -f docker-compose.dev.yml logs -f backend | grep ERROR
```

### Check Container Status
```bash
docker-compose -f docker-compose.dev.yml ps
```

## 🔧 Troubleshooting

### Port Conflicts
If ports are already in use, modify `docker-compose.dev.yml`:

```yaml
services:
  frontend:
    ports:
      - "3000:5173"  # Change 5173 to 3000
  backend:
    ports:
      - "8001:8080"  # Change 8000 to 8001
```

### Dependencies Not Installing
```bash
# Clean rebuild
docker-compose -f docker-compose.dev.yml down -v
docker-compose -f docker-compose.dev.yml build --no-cache
docker-compose -f docker-compose.dev.yml up
```

### Volume Mounting Issues (Windows)
Ensure Docker Desktop has access to your drive:
1. Docker Desktop → Settings → Resources → File Sharing
2. Add `G:\` drive if not listed

### Hot Reload Not Working
```bash
# Restart with clean volumes
docker-compose -f docker-compose.dev.yml down -v
docker-compose -f docker-compose.dev.yml up --build
```

## 📦 Development vs Production

### Development (`docker-compose.dev.yml`)
- ✅ Hot reload enabled
- ✅ Source code mounted as volumes
- ✅ Development dependencies included
- ✅ Detailed logging
- ⚡ Fast iteration

### Production (`docker-compose.yml`)
- ✅ Optimized builds
- ✅ Multi-stage Docker builds
- ✅ Nginx for static serving
- ✅ Health checks
- ✅ Security hardening

## 🧪 Testing in Docker

### Run Frontend Tests
```bash
docker exec leadsniper-frontend-dev npm test
```

### Run Backend Tests
```bash
docker exec leadsniper-backend-dev pytest
```

## 📊 Performance Tips

1. **Use WSL2 on Windows** for better file system performance
2. **Exclude node_modules** from antivirus scanning
3. **Allocate more resources** in Docker Desktop settings (4GB+ RAM, 4+ CPUs)
4. **Use .dockerignore** to exclude unnecessary files from build context

## 🚢 Switching to Production

When ready to test production build:

```bash
# Stop dev environment
docker-compose -f docker-compose.dev.yml down

# Start production environment
docker-compose up --build
```

Access at http://localhost:8080 (production build)

## 💡 Pro Tips

1. **Keep dev running**: Leave containers running, they use minimal resources
2. **Use volumes**: Code changes reflect instantly without rebuild
3. **Check logs**: Use `-f` flag to follow logs in real-time
4. **Clean regularly**: Run `docker system prune` monthly to free space

## 📖 Additional Resources

- Frontend (Vite): https://vitejs.dev/
- Backend (FastAPI): https://fastapi.tiangolo.com/
- Docker Compose: https://docs.docker.com/compose/

---

**Happy Coding! 🎉**
