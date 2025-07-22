from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse, RedirectResponse, StreamingResponse
from .. import crud, schemas, models
from ..database import get_db
import requests
import tempfile
from ..monitoring import clip_view_counter, clip_create_counter

router = APIRouter(prefix="/clips", tags=["clips"])

@router.get("/", response_model=list[schemas.Clip])
def list_clips(db: Session = Depends(get_db)):
    return crud.get_clips(db)

@router.get("/{clip_id}/stream")
def stream_clip(clip_id: int, db: Session = Depends(get_db)):
    clip = crud.increment_play_count(db, clip_id)
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    # Increment Prometheus counter for views
    clip_view_counter.labels(clip_id=str(clip.id), genre=clip.genre).inc()
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(clip.audio_url, stream=True, headers=headers)
    r.raise_for_status()
    return StreamingResponse(r.iter_content(chunk_size=8192), media_type="audio/mpeg")

@router.get("/{clip_id}/stats", response_model=schemas.ClipStats)
def clip_stats(clip_id: int, db: Session = Depends(get_db)):
    clip = crud.get_clip_stats(db, clip_id)
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    return clip

@router.post("/", response_model=schemas.Clip)
def create_clip(clip: schemas.ClipCreate, db: Session = Depends(get_db)):
    # Increment Prometheus counter for creates
    clip_create_counter.labels(genre=clip.genre).inc()
    return crud.create_clip(db, clip)