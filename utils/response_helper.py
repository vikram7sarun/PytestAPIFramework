# utils/response_helper.py

def check_status_code(response, expected_code=200):
    """
    Checks if the response status code matches the expected status code.

    :param response: The response object returned from the request
    :param expected_code: Expected HTTP status code (default is 200)
    :raises AssertionError: If the status code does not match
    """
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, but got {response.status_code}"
    )


def check_json_key(response, key, expected_value=None):
    """
    Checks if a specific key exists in the JSON response and optionally checks its value.

    :param response: The response object with JSON data
    :param key: The key to check in the JSON response
    :param expected_value: Optional expected value to check against the key
    :raises AssertionError: If the key is missing or the value does not match
    """
    json_data = response.json()
    assert key in json_data, f"Key '{key}' not found in response JSON"

    if expected_value is not None:
        assert json_data[key] == expected_value, (
            f"Expected value for '{key}' to be '{expected_value}', but got '{json_data[key]}'"
        )


def check_response_time(response, max_time=1):
    """
    Verifies that the response time is within the expected limit.

    :param response: The response object from the request
    :param max_time: Maximum allowable response time in seconds (default is 1 second)
    :raises AssertionError: If the response time exceeds the max_time
    """
    assert response.elapsed.total_seconds() <= max_time, (
        f"Response time exceeded {max_time} seconds: {response.elapsed.total_seconds()} seconds"
    )


def check_response_contains(response, content):
    """
    Checks if the response content contains a specific string or data.

    :param response: The response object from the request
    :param content: The content expected to be found in the response text
    :raises AssertionError: If the content is not found
    """
    assert content in response.text, f"'{content}' not found in response text"
