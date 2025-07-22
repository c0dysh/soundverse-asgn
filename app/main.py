from fastapi import FastAPI
from .routes import clips
from .monitoring import setup_monitoring
from .database import engine
from .models import Base

app = FastAPI(title="Soundverse Clips API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(clips.router)
setup_monitoring(app) 