import pytest
from utils.request_helper import post_request
from utils.response_helper import check_status_code, check_json_key


@pytest.mark.parametrize("name, email", [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
])
def test_create_user_with_different_data(api_client, base_url, name, email, logger):
    logger.info(f"Starting test_create_user_with_different_data for {name}")
    payload = {"name": name, "email": email}

    logger.info(f"Payload: {payload}")
    response = post_request(api_client, "users", base_url, json_data=payload)

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    check_status_code(response, 201)
    check_json_key(response, "name", name)
    check_json_key(response, "email", email)
    logger.info(f"test_create_user_with_different_data for {name} passed successfully")
