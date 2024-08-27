from lib.json_schema import get_schema_by_json
from testcase.swapi.schema.json_res_sample import JsonResSample


class Schema:

    @property
    @get_schema_by_json
    def get_people(self):
        return JsonResSample.get_people_example

    @property
    @get_schema_by_json
    def get_vehicles(self):
        return JsonResSample.get_vehicles_example


if __name__ == "__main__":
    pass
