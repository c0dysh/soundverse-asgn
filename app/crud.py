from sqlalchemy.orm import Session
from . import models, schemas

# Get all clips
def get_clips(db: Session):
    return db.query(models.Clip).all()

# Get a single clip by id
def get_clip(db: Session, clip_id: int):
    return db.query(models.Clip).filter(models.Clip.id == clip_id).first()

# Increment play count
def increment_play_count(db: Session, clip_id: int):
    clip = get_clip(db, clip_id)
    if clip:
        clip.play_count += 1
        db.commit()
        db.refresh(clip)
    return clip

# Create a new clip
def create_clip(db: Session, clip: schemas.ClipCreate):
    db_clip = models.Clip(**clip.dict())
    db.add(db_clip)
    db.commit()
    db.refresh(db_clip)
    return db_clip

# Get stats for a clip
def get_clip_stats(db: Session, clip_id: int):
    return get_clip(db, clip_id) 