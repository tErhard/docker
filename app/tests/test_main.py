from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"message": "Read all items"}  # Перевірка очікуваної відповіді

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Read item with ID 1"}  # Перевірка очікуваної відповіді
