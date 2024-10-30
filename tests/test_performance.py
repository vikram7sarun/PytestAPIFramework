from utils.request_helper import get_request
from utils.response_helper import check_status_code, check_response_time

def test_response_time_for_get_user(api_client, base_url):
    user_id = 1
    response = get_request(api_client, f"users/{user_id}", base_url)
    check_status_code(response, 200)
    check_response_time(response, max_time=0.5)
