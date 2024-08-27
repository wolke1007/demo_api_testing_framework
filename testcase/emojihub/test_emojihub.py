import asyncio
import sys

import pytest
import allure
from typing import Final

from testcase.emojihub.schema.schema import Schema

"""
EmojiHub
'Get emojis by categories and groups'
https://github.com/cheatsnake/emojihub

Auth:   No
HTTPS:  YES
CORS:   Yes
"""

EMOJIHUB_BASE_URL: Final = "https://emojihub.yurace.pro/api/"

json_schema_obj = Schema()
testcase_1_params = [
    ('random/group/face-positive', 200, json_schema_obj.get_random_emoji),
    ('random/category/food-and-drink', 200, json_schema_obj.get_random_emoji),
    ('random/category/non-exist', 404, json_schema_obj.get_category_not_exist),
    ('random/abc/non-exist', 404, None),
    ('all/group/animal-bird', 200, json_schema_obj.get_all_emoji)
]

all_smileys_and_people_groups = ['body', 'cat-face', 'clothing', 'creature-face', 'emotion', 'face-negative',
                                 'face-neutral', 'face-positive', 'face-positive', 'face-role', 'face-sick', 'family',
                                 'monkey-face', 'person', 'person-activity', 'person-gesture', 'person-role',
                                 'skin-tone']
testcase_2_params = [
    [
        ('random/group/' + group, 200, json_schema_obj.get_random_emoji) for group in all_smileys_and_people_groups
    ]
]


class TestEmojihub:

    @pytest.mark.emojihub
    @allure.testcase('EmojiHub API Test 1')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("api_path, expect_status_code, json_schema", testcase_1_params)
    def test_get_emoji(self, api_path: str, expect_status_code: int, json_schema: dict, setup_base_api):
        url = f"{EMOJIHUB_BASE_URL}{api_path}"
        base_api = setup_base_api
        response = base_api.get(url)
        base_api.validate_status_code(response, expect_status_code)
        base_api.validate_json(response, expect_json_schema=json_schema)

    @pytest.mark.asyncio
    @pytest.mark.emojihub
    @allure.testcase('EmojiHub API Test 2')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skipif(sys.version_info < (3, 11), reason="requires Python 3.11 or higher")
    @pytest.mark.parametrize("test_data", testcase_2_params)
    async def test_async_get_emojis(self, test_data: list, setup_base_api):
        """
        Run 18 emojis test in async mode.
        :param test_data: List of test data sets, where each set includes vehicle_id, expected status code, and JSON schema.
        :param setup_base_api: Fixture providing a setup instance of the BaseAPI class.
        """
        base_api = setup_base_api

        # Create a list of tasks to be run concurrently
        tasks = []
        for data_set in test_data:
            api_path, expect_status_code, json_schema = data_set
            url = f"{EMOJIHUB_BASE_URL}{api_path}"
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
