#!/bin/sh
set -e

# Wait for the database to be ready
until pg_isready -h db -p 5432 -U postgres; do
  echo "Waiting for postgres..."
  sleep 2
done

# Seed the database (ignore errors if already seeded)
python seed_clips.py || true

# Start the FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 