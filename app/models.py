from sqlalchemy import Column, Integer, String
from .database import Base

class Clip(Base):
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    audio_url = Column(String, nullable=False)
    play_count = Column(Integer, default=0) 