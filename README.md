# Soundverse Clips Backend

A FastAPI backend for lightweight audio previews ("Clips") with PostgreSQL, Prometheus monitoring, and deployment-ready setup.

## Features

- List available sound clips
- Stream a specific clip (real-time streaming, increments play count)
- Get play count and metadata for a clip
- Prometheus metrics for monitoring
- (Bonus) Add new clips via API

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Prometheus + Grafana (via starlette_exporter)
- Docker & Docker Compose
- Render/Railway/Vercel deployment

## Project Structure

```
soundverse-asgn/
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # DB operations
│   ├── database.py        # DB connection/session
│   ├── routes/
│   │   └── clips.py       # All /clips endpoints
│   └── monitoring.py      # Prometheus integration
│
├── seed_clips.py          # DB seeding script
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example           # Example env file
├── README.md
├── .gitignore
└── tests/
    └── test_clips.py      # API tests
```

## Setup

### Local Development

1. **Clone & Install**
   ```bash
   git clone <your-repo-url>
   cd soundverse-asgn
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Configure DB**
   - Set `DATABASE_URL` in `.env` (see `.env.example`).
   - Example: `postgresql://postgres:postgres@localhost:5432/soundverse`
3. **Seed Database**
   ```bash
   python seed_clips.py
   ```
4. **Run Locally**
   ```bash
   uvicorn app.main:app --reload
   ```

### Dockerized Setup

1. **Build and Start Containers**
   ```bash
   docker-compose up --build
   ```
   - App: http://localhost:8000 (or 8001 if mapped)
   - DB: localhost:5432 (user: postgres, password: postgres, db: soundverse)
2. **Seed the Database (in a running container)**
   ```bash
   docker-compose exec web python seed_clips.py
   ```
3. **Run Tests (in a running container)**
   ```bash
   docker-compose exec web pytest tests/
   ```

## API Endpoints

- `GET /clips` — List all clips
- `GET /clips/{id}/stream` — Real-time stream audio, increments play count
- `GET /clips/{id}/stats` — Get play count and metadata
- `POST /clips` — (Bonus) Add a new clip

## Monitoring

- Prometheus metrics at `/metrics`
- Add to Grafana dashboard for visualization
- Example metrics: total API requests, streams by clip ID, response latency

## Deployment

- Deploy on [Render](https://render.com/), [Railway](https://railway.app/), or [Vercel](https://vercel.com/)
- Set environment variables for DB credentials
- Expose only to internal/private networks if required

## Troubleshooting

- **403 on streaming:** Use only public MP3 URLs that allow server-side access (see `seed_clips.py`).
- **High latency:** Real-time streaming is implemented; for even lower latency, host files locally.
- **Already seeded:** Clear the DB or use `docker-compose down -v` to reset.

## Credits

- [SoundHelix](https://www.soundhelix.com/) and [file-examples.com](https://file-examples.com/) for public domain MP3s.
- [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/)

## License

MIT
