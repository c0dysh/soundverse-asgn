import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
from app.database import SessionLocal, engine
from app.models import Base, Clip

# Ensure tables are created before seeding
Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    if db.query(Clip).count() > 0:
        print("Already seeded.")
        return
    clips = [
        Clip(
            title="Ambient Forest",
            description="Relaxing forest ambience.",
            genre="ambient",
            duration="30s",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        ),
        Clip(
            title="Pop Beat",
            description="Upbeat pop instrumental.",
            genre="pop",
            duration="30s",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        ),
        Clip(
            title="Electronic Groove",
            description="Futuristic electronic groove.",
            genre="electronic",
            duration="30s",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        ),
        Clip(
            title="Chillhop Vibes",
            description="Laid-back chillhop track.",
            genre="hiphop",
            duration="30s",
            audio_url="https://file-examples.com/storage/fe6b7e2e2e2e2e2e2e2e2e2e2e2e2e2e/audio/mp3/file_example_MP3_700KB.mp3"
        ),
        Clip(
            title="Classical Piano",
            description="Soothing classical piano piece.",
            genre="classical",
            duration="30s",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
        ),
        Clip(
            title="Rock Riff",
            description="Energetic rock guitar riff.",
            genre="rock",
            duration="30s",
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
        ),
    ]
    db.add_all(clips)
    db.commit()
    print("Seeded 6 clips.")
    db.close()

if __name__ == "__main__":
    seed() 