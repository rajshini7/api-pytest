import pytest
from client.api_client import APIClient
from data.post_payloads import create_post_payload

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def created_post(api_client):
    response = api_client.post("/posts", create_post_payload())
    assert response.status_code == 201

    post_id = response.json()["id"]

    yield post_id

    # cleanup (important)
    api_client.delete(f"/posts/{post_id}")
