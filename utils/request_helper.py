# utils/request_helper.py

import requests
from config.config import API_KEY


def make_request(session, method, endpoint, base_url, data=None, headers=None, params=None, json_data=None):
    """
    A generic request function that can handle all HTTP methods.

    :param session: The session object to maintain connection
    :param method: HTTP method (GET, POST, PUT, DELETE, etc.)
    :param endpoint: The endpoint path to hit
    :param base_url: The base URL for the API
    :param data: Form data for POST/PUT requests
    :param headers: Headers dictionary
    :param params: URL parameters
    :param json_data: JSON data for POST/PUT requests
    :return: Response object
    """
    url = f"{base_url}/{endpoint}"
    headers = headers or {}
    headers.update({"Authorization": f"Bearer {API_KEY}"})

    response = session.request(method, url, data=data, headers=headers, params=params, json=json_data)
    return response


def get_request(session, endpoint, base_url, headers=None, params=None):
    """
    Sends a GET request.

    :param session: Session object
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param headers: Optional headers
    :param params: Optional query parameters
    :return: Response object
    """
    return make_request(session, 'GET', endpoint, base_url, headers=headers, params=params)


def post_request(session, endpoint, base_url, json_data=None, headers=None, data=None, params=None):
    """
    Sends a POST request with optional JSON or form data.

    :param session: Session object
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param json_data: JSON payload for the request
    :param headers: Optional headers
    :param data: Optional form data
    :param params: Optional query parameters
    :return: Response object
    """
    return make_request(session, 'POST', endpoint, base_url, data=data, headers=headers, params=params,
                        json_data=json_data)


def put_request(session, endpoint, base_url, json_data=None, headers=None, data=None, params=None):
    """
    Sends a PUT request with optional JSON or form data.

    :param session: Session object
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param json_data: JSON payload for the request
    :param headers: Optional headers
    :param data: Optional form data
    :param params: Optional query parameters
    :return: Response object
    """
    return make_request(session, 'PUT', endpoint, base_url, data=data, headers=headers, params=params,
                        json_data=json_data)


def delete_request(session, endpoint, base_url, headers=None, params=None):
    """
    Sends a DELETE request.

    :param session: Session object
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param headers: Optional headers
    :param params: Optional query parameters
    :return: Response object
    """
    return make_request(session, 'DELETE', endpoint, base_url, headers=headers, params=params)


def patch_request(session, endpoint, base_url, json_data=None, headers=None, data=None, params=None):
    """
    Sends a PATCH request with optional JSON or form data.

    :param session: Session object
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param json_data: JSON payload for the request
    :param headers: Optional headers
    :param data: Optional form data
    :param params: Optional query parameters
    :return: Response object
    """
    return make_request(session, 'PATCH', endpoint, base_url, data=data, headers=headers, params=params,
                        json_data=json_data)


def upload_file(session, endpoint, base_url, file_path, headers=None):
    """
    Sends a POST request to upload a file.

    :param session: Session object
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param file_path: Path to the file to be uploaded
    :param headers: Optional headers
    :return: Response object
    """
    url = f"{base_url}/{endpoint}"
    with open(file_path, 'rb') as file:
        files = {'file': file}
        headers = headers or {}
        headers.update({"Authorization": f"Bearer {API_KEY}"})
        response = session.post(url, files=files, headers=headers)
    return response


def retry_request(session, method, endpoint, base_url, retries=3, **kwargs):
    """
    Retries a request up to a specified number of times in case of failure.

    :param session: Session object
    :param method: HTTP method (GET, POST, etc.)
    :param endpoint: Endpoint path
    :param base_url: Base URL for the API
    :param retries: Number of retries
    :param kwargs: Additional arguments to pass to the request
    :return: Response object
    """
    for attempt in range(retries):
        response = make_request(session, method, endpoint, base_url, **kwargs)
        if response.status_code == 200:
            return response
        print(f"Attempt {attempt + 1} failed with status {response.status_code}. Retrying...")
    return response  # Return the last response if all retries fail
