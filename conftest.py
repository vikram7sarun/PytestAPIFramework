# conftest.py
import pytest
import requests
from config.config import BASE_URL

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def api_client():
    session = requests.Session()
    yield session
    session.close()

# conftest.py
import logging

def pytest_configure():
    logging.basicConfig(filename='logs/api_test.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')



@pytest.fixture(scope="session")
def fake_data():
    pass
    # return Faker()


def pytest_configure():
    logging.basicConfig(
        filename='logs/api_test.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

@pytest.fixture(scope="function")
def logger():
    return logging.getLogger("api_test_logger")