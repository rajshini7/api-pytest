def create_post_payload():
    return {
        "title": "Initial Post",
        "body": "This is a test post",
        "userId": 1
    }

def update_post_payload():
    return {
        "title": "Updated Post",
        "body": "Post updated using PUT",
        "userId": 1
    }

def patch_post_payload():
    return {
        "title": "Patched Title"
    }
