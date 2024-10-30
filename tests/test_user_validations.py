from utils.request_helper import post_request, get_request
from utils.response_helper import check_status_code, check_json_key

def test_create_user_missing_required_fields(api_client, base_url):
    payload = {"name": ""}
    response = post_request(api_client, "users", base_url, json_data=payload)
    check_status_code(response, 400)
    check_json_key(response, "error")

def test_get_nonexistent_user(api_client, base_url):
    non_existent_user_id = 9999
    response = get_request(api_client, f"users/{non_existent_user_id}", base_url)
    check_status_code(response, 404)
    check_json_key(response, "error")
