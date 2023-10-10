import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_server_health(client):
    # Test server health
    response = client.get('/api/v1/')
    assert response.status_code == 200
    assert b'{"message": "server is up and running"}' in response.data
