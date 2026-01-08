from data.post_payloads import update_post_payload, patch_post_payload

def test_create_post(api_client):
    response = api_client.post("/posts", {
        "title": "Create Test",
        "body": "Create body",
        "userId": 1
    })
    assert response.status_code == 201


def test_get_post(api_client, created_post):
    response = api_client.get(f"/posts/{created_post}")
    assert response.status_code == 200


def test_put_post(api_client, created_post):
    response = api_client.put(
        f"/posts/{created_post}",
        update_post_payload()
    )
    assert response.status_code == 200


def test_patch_post(api_client, created_post):
    response = api_client.patch(
        f"/posts/{created_post}",
        patch_post_payload()
    )
    assert response.status_code == 200


def test_delete_post(api_client, created_post):
    response = api_client.delete(f"/posts/{created_post}")
    assert response.status_code == 200
