import asyncio
import logging

import pytest
import allure
from urllib.error import HTTPError, URLError
from jsonschema import validate, ValidationError
import json


class BaseAPI:
    """Main base class for Requests based scripts."""

    def __init__(self, request_obj):
        self.request_obj = request_obj
        self.logger = logging.getLogger(__name__)

    @allure.step("Validate json by stored schema")
    def validate_json(self, response: dict, expect_json_schema: dict) -> None:
        if expect_json_schema is None:
            return
        try:
            json_response = response['json_response']
            validate(instance=json_response, schema=expect_json_schema)
        except ValidationError as e:
            self.logger.error('JSON response:\n%s', json.dumps(json_response, indent=2))
            self.logger.error('Expected JSON schema:\n%s', json.dumps(expect_json_schema, indent=2))
            self.logger.error('Validation error: %s', e.message)
            pytest.fail(f"JSON format is invalid: {e.message}")

    @allure.step("Validate response status code is {expect_status_code}")
    def validate_status_code(self, response: dict, expect_status_code: int) -> None:
        assert response['status_code'] == expect_status_code

    @allure.step("GET request to {url}")
    def get(self, url, headers=None):
        """Get request."""
        headers = headers if headers else {}
        try:
            response = self.request_obj.get(url=url, headers=headers)
            json_response = self._get_json_response(response)
            return {'status_code': response.status_code, 'text': response.text, 'json_response': json_response}
        except (HTTPError, URLError) as e:
            self._log_error(e, url)
            raise
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {str(e)}", pytrace=True)

    @allure.step("POST request to {url}")
    def post(self, url, params=None, data=None, json=None, headers=None):
        """Post request."""
        headers = headers if headers else {}
        try:
            response = self.request_obj.post(url, params=params, json=json, headers=headers)
            json_response = self._get_json_response(response)
            return {'status_code': response.status_code, 'text': response.text, 'json_response': json_response}
        except (HTTPError, URLError) as e:
            self._log_error(e, url)
            raise
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {str(e)}", pytrace=True)

    @allure.step("DELETE request to {url}")
    def delete(self, url, headers=None):
        """Delete request."""
        headers = headers if headers else {}
        try:
            response = self.request_obj.delete(url, headers=headers)
            json_response = self._get_json_response(response)
            return {'status_code': response.status_code, 'text': response.text, 'json_response': json_response}
        except (HTTPError, URLError) as e:
            self._log_error(e, url)
            raise
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {str(e)}", pytrace=True)

    @allure.step("PUT request to {url}")
    def put(self, url, json=None, headers=None):
        """Put request."""
        headers = headers if headers else {}
        try:
            response = self.request_obj.put(url, json=json, headers=headers)
            json_response = self._get_json_response(response)
            return {'status_code': response.status_code, 'text': response.text, 'json_response': json_response}
        except (HTTPError, URLError) as e:
            self._log_error(e, url)
            raise
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {str(e)}", pytrace=True)

    @allure.step("Async GET request to {url}")
    async def async_get(self, url, headers=None):
        """Run the blocking GET method in a thread."""
        return await asyncio.to_thread(self.get, url, headers)

    @allure.step("Async POST request to {url}")
    async def async_post(self, url, params=None, data=None, json=None, headers=None):
        """Run the blocking POST method in a thread."""
        return await asyncio.to_thread(self.post, url, params, data, json, headers)

    @allure.step("Async DELETE request to {url}")
    async def async_delete(self, url, headers=None):
        """Run the blocking DELETE method in a thread."""
        return await asyncio.to_thread(self.delete, url, headers)

    @allure.step("Async PUT request to {url}")
    async def async_put(self, url, json=None, headers=None):
        """Run the blocking PUT method in a thread."""
        return await asyncio.to_thread(self.put, url, json, headers)

    def _get_json_response(self, response):
        """Helper method to parse JSON response."""
        try:
            return response.json()
        except Exception:
            return None

    def _log_error(self, e, url):
        """Helper method to log errors."""
        if isinstance(e, HTTPError):
            allure.attach(body=e.read(), name="HTTP Error Response", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"HTTPError: {url} - {e}")
        elif isinstance(e, URLError):
            if e.reason.args[0] == 10061:
                pytest.fail("URL open error: Please check if the API server is up or there is any other issue accessing the URL.")
            else:
                pytest.fail(f"URLError: {url} - {e.reason.args}")
        else:
            pytest.fail(f"Unexpected error: {url} - {str(e)}")
