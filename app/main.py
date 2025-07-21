from fastapi import FastAPI
from .routes import clips
from .monitoring import setup_monitoring

app = FastAPI(title="Soundverse Clips API")

app.include_router(clips.router)
setup_monitoring(app) 