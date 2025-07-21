import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_clips():
    response = client.get("/clips/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 5

def test_clip_stats():
    response = client.get("/clips/1/stats")
    assert response.status_code == 200
    data = response.json()
    assert "play_count" in data
    assert "title" in data

def test_stream_clip():
    response = client.get("/clips/1/stream")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("audio/") 