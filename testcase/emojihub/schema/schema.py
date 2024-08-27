from lib.json_schema import get_schema_by_json
from testcase.emojihub.schema.json_res_sample import JsonResSample


class Schema:

    @property
    @get_schema_by_json
    def get_random_emoji(self):
        """
        all random emoji use this schema
        :return:
        """
        return JsonResSample.emoji

    @property
    @get_schema_by_json
    def get_category_not_exist(self):
        return JsonResSample.category_not_exist

    @property
    @get_schema_by_json
    def get_all_emoji(self):
        return JsonResSample.all_emoji


if __name__ == "__main__":
    pass
