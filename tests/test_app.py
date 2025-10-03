import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello DevOps" in response.data

def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"http_requests_total" in response.data
