import pytest
import json
from unittest.mock import patch
from functools import wraps

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {
    "id": "28a3ad77-7d3c-47e3-9c42-858ca3ec5222",
    "role": 2
}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/exercise/ping")
    assert response.status_code == 200
    assert b"pong" in response.data

def test_request_post(client):
    url = "/training-plan"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "user":"29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
        "days": [
            {
                "day": "Monday",
                "exercises": [
                    {
                        "id": "24deef23-bf8e-4c14-884d-c4e1fd5c62c3"
                    }
                ]
            },
            {
                "day": "Wednesday",
                "exercises": [
                    {
                        "id": "24deef23-bf8e-4c14-884d-c4e1fd5c62c3"
                    },
                    {
                        "id": "24deef23-bf8e-4c14-884d-c4e1fd5c62c3"
                    }
                ]
            }
        ]
}
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201


def test_request_get(client):
    url = "/training-plan"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "user":"29a3ad78-6d3c-46e3-9c42-857ca3ec5220",
        "days": [
            {
                "day": "Monday",
                "exercises": [
                    {
                        "id": "24deef23-bf8e-4c14-884d-c4e1fd5c62c3"
                    }
                ]
            },
            {
                "day": "Wednesday",
                "exercises": [
                    {
                        "id": "24deef23-bf8e-4c14-884d-c4e1fd5c62c3"
                    },
                    {
                        "id": "24deef23-bf8e-4c14-884d-c4e1fd5c62c3"
                    }
                ]
            }
        ]
}
    client.post(url, data=json.dumps(data), headers=headers)
    response = client.get("/training-plan")
    assert response.status_code == 200
    assert b"plans" in response.data
