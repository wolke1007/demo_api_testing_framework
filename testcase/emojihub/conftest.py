import requests
from lib.base_api import BaseAPI
import pytest


@pytest.fixture
def setup_base_api():
    base_api = BaseAPI(requests)
    yield base_api
