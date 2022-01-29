from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200


def test_books_resource():
    response_auth = client.get(f"/api/v1/books")
    assert response_auth.status_code == 200
