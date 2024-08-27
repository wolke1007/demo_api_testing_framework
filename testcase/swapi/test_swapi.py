import asyncio
import sys

import pytest
import allure
from typing import Final

from testcase.swapi.schema.schema import Schema

"""
SWAPI
'All things Star Wars'

Auth:   No
HTTPS:  YES
CORS:   Yes
"""

SWAPI_BASE_URL: Final = "https://swapi.dev/api/"

json_schema_obj = Schema()
testcase_1_params = [
    (1, 200, json_schema_obj.get_people),   # Valid people ID
    (10, 200, json_schema_obj.get_people),  # Valid people ID
    (10000, 404, None),                     # Non-existent people ID
]

testcase_2_params = [
    (4, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
    (6, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
    (1, 404, None),                             # Non-existent vehicles ID
]

testcase_3_params = [
    [
        (4, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (6, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (1, 404, None),                             # Non-existent vehicles ID
        (4, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (6, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (1, 404, None),                             # Non-existent vehicles ID
        (4, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (6, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (1, 404, None),                             # Non-existent vehicles ID
        (4, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (6, 200, json_schema_obj.get_vehicles),     # Valid vehicles ID
        (1, 404, None),                             # Non-existent vehicles ID
    ],
]


class TestSwapi:

    @pytest.mark.swapi
    @allure.testcase('SWAPI API Test 1')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("people_id, expect_status_code, json_schema", testcase_1_params)
    def test_get_people_info(self, people_id: int, expect_status_code: int, json_schema: dict, setup_base_api):
        url = f"{SWAPI_BASE_URL}people/{people_id}"
        base_api = setup_base_api
        response = base_api.get(url)
        base_api.validate_status_code(response, expect_status_code)
        base_api.validate_json(response, expect_json_schema=json_schema)

    @pytest.mark.swapi
    @allure.testcase('SWAPI API Test 2')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("vehicle_id, expect_status_code, json_schema", testcase_2_params)
    def test_get_vehicle_info(self, vehicle_id: int, expect_status_code: int, json_schema: dict, setup_base_api):
        url = f"{SWAPI_BASE_URL}vehicles/{vehicle_id}"
        base_api = setup_base_api
        response = base_api.get(url)
        base_api.validate_status_code(response, expect_status_code)
        base_api.validate_json(response, expect_json_schema=json_schema)

    @pytest.mark.asyncio
    @pytest.mark.swapi
    @allure.testcase('SWAPI API Test 3')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skipif(sys.version_info < (3, 11), reason="requires Python 3.11 or higher")
    @pytest.mark.parametrize("test_data", testcase_3_params)
    async def test_async_get_vehicles(self, test_data: list, setup_base_api):
        """
        Run 12 vehicles test in async mode.
        :param test_data: List of test data sets, where each set includes vehicle_id, expected status code, and JSON schema.
        :param setup_base_api: Fixture providing a setup instance of the BaseAPI class.
        """
        base_api = setup_base_api

        # Create a list of tasks to be run concurrently
        tasks = []
        for data_set in test_data:
            vehicle_id, expect_status_code, json_schema = data_set
            url = f"{SWAPI_BASE_URL}vehicles/{vehicle_id}"
            task = base_api.async_get(url)
            tasks.append(task)

        # Run all tasks concurrently and wait for them to complete
        results = await asyncio.gather(*tasks)

        # Validate the results
        for index, (response, data_set) in enumerate(zip(results, test_data), start=1):
            _, expect_status_code, json_schema = data_set
            with allure.step(f"Validate {index}-th data set response"):
                base_api.validate_status_code(response, expect_status_code)
                base_api.validate_json(response, expect_json_schema=json_schema)
