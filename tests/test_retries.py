from utils.request_helper import retry_request
from utils.response_helper import check_status_code, check_json_key


def test_get_user_with_retries(api_client, base_url, logger):
    logger.info("Starting test_get_user_with_retries")
    user_id = 1

    response = retry_request(api_client, 'GET', f"users/{user_id}", base_url, retries=3)

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    check_status_code(response, 200)
    check_json_key(response, "id", user_id)
    logger.info("test_get_user_with_retries passed successfully")
