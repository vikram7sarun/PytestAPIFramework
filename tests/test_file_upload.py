from utils.request_helper import upload_file
from utils.response_helper import check_status_code, check_json_key

def test_upload_user_profile_picture(api_client, base_url, logger):
    logger.info("Starting test_upload_user_profile_picture")
    user_id = 1
    file_path = "path/to/profile_picture.jpg"

    logger.info(f"File path for upload: {file_path}")
    response = upload_file(api_client, f"users/{user_id}/upload", base_url, file_path=file_path)

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json()}")

    check_status_code(response, 200)
    check_json_key(response, "message", "File uploaded successfully")
    logger.info("test_upload_user_profile_picture passed successfully")
