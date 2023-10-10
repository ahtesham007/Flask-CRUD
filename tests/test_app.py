import pytest
from app import app
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URI = "/api/v1"


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_server_health(client):
    # Test server health
    response = client.get(f'{BASE_URI}/')
    assert response.status_code == 200
    assert b'{"message": "server is up and running"}' in response.data

def test_create_user(client):
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com"
    }

    response = client.post(f'{BASE_URI}/users/', json=user_data)

    assert response.status_code == 201


def test_update_user(client):
    user_data = {
        "data": {
            "username": "testuser_update",
            "email": "test@gmail.com"
        },
        "id": "6524e6c4e2d53767025e0e1e"

    }

    response = client.put(f'{BASE_URI}/users/', json=user_data)

    assert response.status_code == 202
    assert b'{"message": "Successfully Updated"}' in response.data
