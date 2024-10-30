import pytest
from utils.request_helper import post_request, get_request, put_request, delete_request
from utils.response_helper import check_status_code, check_json_key

@pytest.mark.smoke
@pytest.mark.regression
def test_create_user(api_client, base_url,logger):
    logger.info("Starting test_create_user")
    payload = {"name": "John Doe", "email": "john.doe@example.com"}

    logger.info(f"Payload for creating user: {payload}")
    response = post_request(api_client, "users", base_url, json_data=payload)

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    check_status_code(response, 201)
    check_json_key(response, "id")
    check_json_key(response, "name", "John Doe")
    logger.info("test_create_user passed successfully")

@pytest.mark.regression
def test_get_user(api_client, base_url, logger):
    logger.info("Starting test_get_user")
    user_id = 1

    response = get_request(api_client, f"users/{user_id}", base_url)

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    check_status_code(response, 200)
    check_json_key(response, "id", user_id)
    logger.info("test_get_user passed successfully")

@pytest.mark.regression
def test_update_user(api_client, base_url, logger):
    logger.info("Starting test_update_user")
    user_id = 1
    payload = {"name": "Jane Doe", "email": "jane.doe@example.com"}

    logger.info(f"Payload for updating user: {payload}")
    response = put_request(api_client, f"users/{user_id}", base_url, json_data=payload)

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    check_status_code(response, 200)
    check_json_key(response, "name", "Jane Doe")
    logger.info("test_update_user passed successfully")

@pytest.mark.regression
def test_delete_user(api_client, base_url, logger):
    logger.info("Starting test_delete_user")
    user_id = 1

    response = delete_request(api_client, f"users/{user_id}", base_url)

    logger.info(f"Response status code: {response.status_code}")

    check_status_code(response, 204)
    logger.info("test_delete_user passed successfully")
