from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_add_endpoint():
    response = client.get("/add?a=3&b=4")
    assert response.status_code == 200
    assert response.json()["result"] == 7
