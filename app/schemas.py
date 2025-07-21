from pydantic import BaseModel

class ClipBase(BaseModel):
    title: str
    description: str
    genre: str
    duration: str
    audio_url: str

class ClipCreate(ClipBase):
    pass

class Clip(ClipBase):
    id: int
    play_count: int

    class Config:
        orm_mode = True

class ClipStats(BaseModel):
    id: int
    title: str
    play_count: int
    description: str
    genre: str
    duration: str
    audio_url: str

    class Config:
        orm_mode = True 