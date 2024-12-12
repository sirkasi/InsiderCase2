import pytest
import requests
import random

BASE_URL = "https://petstore.swagger.io/v2"
PET_ENDPOINT = f"{BASE_URL}/pet"

@pytest.fixture
def random_pet_id():
    return random.randint(100000, 999999)

def test_create_pet_positive(random_pet_id):
    payload = {
        "id": random_pet_id,
        "name": "Fluffy",
        "photoUrls": ["https://example.com/fluffy.jpg"],
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
    r = requests.post(PET_ENDPOINT, json=payload)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    response_data = r.json()
    assert response_data['id'] == random_pet_id, "ID does not match"
    assert response_data['name'] == "Fluffy", "Name does not match"

def test_get_pet_positive(random_pet_id):
    # First create the pet
    create_payload = {"id": random_pet_id, "name": "CheckGet", "photoUrls": ["url"], "status": "available"}
    requests.post(PET_ENDPOINT, json=create_payload)

    # Now get the pet
    r = requests.get(f"{PET_ENDPOINT}/{random_pet_id}")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    response_data = r.json()
    assert response_data['id'] == random_pet_id

def test_update_pet_positive(random_pet_id):
    # Create Pet
    create_payload = {"id": random_pet_id, "name": "ToUpdate", "photoUrls": ["url"], "status": "available"}
    requests.post(PET_ENDPOINT, json=create_payload)

    # Update Pet
    update_payload = {"id": random_pet_id, "name": "UpdatedName", "photoUrls": ["url"], "status": "sold"}
    r = requests.put(PET_ENDPOINT, json=update_payload)
    assert r.status_code == 200
    response_data = r.json()
    assert response_data['name'] == "UpdatedName"
    assert response_data['status'] == "sold"

def test_delete_pet_positive(random_pet_id):
    # Create Pet
    create_payload = {"id": random_pet_id, "name": "ToDelete", "photoUrls": ["url"], "status": "available"}
    requests.post(PET_ENDPOINT, json=create_payload)

    # Delete Pet
    r = requests.delete(f"{PET_ENDPOINT}/{random_pet_id}")
    assert r.status_code == 200

    # Try to GET again - should not be found
    r = requests.get(f"{PET_ENDPOINT}/{random_pet_id}")
    assert r.status_code == 404

# Negative scenarios

def test_get_non_existing_pet():
    # Try to get a non-existing pet
    non_existing_id = 99999999999
    r = requests.get(f"{PET_ENDPOINT}/{non_existing_id}")
    assert r.status_code == 404

def test_delete_non_existing_pet():
    non_existing_id = 88888888888
    r = requests.delete(f"{PET_ENDPOINT}/{non_existing_id}")
    assert r.status_code in [404, 400], f"Unexpected status code: {r.status_code}"

def test_create_pet_invalid_data_type():
    # Sending a payload that doesn't conform to expected schema
    # For instance, a string instead of a JSON object
    r = requests.post(PET_ENDPOINT, data="JustAString")
    assert r.status_code == 415, f"Unexpected status code: {r.status_code}"

def test_create_pet_empty_name(random_pet_id):
    payload = {
        "id": random_pet_id,
        "name": "",  # Empty name
        "photoUrls": ["https://example.com/pet.jpg"],
        "status": "available"
    }
    r = requests.post(PET_ENDPOINT, json=payload)
    assert r.status_code == 200, f"Unexpected status code: {r.status_code}"
