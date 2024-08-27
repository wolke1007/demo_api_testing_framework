from functools import wraps


def infer_schema(data):
    """
    This is from outer project generate-json-schema and edit by CloudChen
    https://pypi.org/project/generate-json-schema/

    Infer the JSON schema from the provided data.

    Args:
        data: The data for which the schema needs to be inferred.

    Returns:
        dict: The JSON schema describing the data structure.
    """
    if isinstance(data, dict):
        # For dictionaries, infer the schema of each value recursively
        properties = {}
        for key, value in data.items():
            properties[key] = infer_schema(value)

        # Create the schema for object type
        schema = {
            "type": "object",
            "properties": properties
        }
        return schema

    elif isinstance(data, list):
        if not data:
            # If the list is empty, define it as an array with unknown items
            return {"type": "array", "items": {}}

        # Infer the schema of each element in the list
        item_schemas = [infer_schema(item) for item in data]

        # If all items in the list have the same schema, use that schema
        # Otherwise, use a schema that allows any type
        first_item_schema = item_schemas[0]
        if all(item == first_item_schema for item in item_schemas):
            return {"type": "array", "items": first_item_schema}
        else:
            return {"type": "array", "items": {"type": "object"}}  # Or a more general schema

    elif isinstance(data, bool):
        # For booleans, return the corresponding JSON schema
        return {"type": "boolean"}

    elif isinstance(data, int):
        # For integers, return the corresponding JSON schema
        return {"type": "integer"}

    elif isinstance(data, float):
        # For floats, return the corresponding JSON schema
        return {"type": "number"}

    elif isinstance(data, str):
        # For strings, return the corresponding JSON schema
        return {"type": "string"}

    else:
        # For other data types, assume null
        return {"type": "null"}


# 定義 get_schema_by_json 裝飾器
def get_schema_by_json(func):
    """
    json to json schema
    e.q.
    json
    {
      "name": "Luke Skywalker"
    }

    json schema
    {
    "type": "object",
    "properties": {
      "name": {"type": "string"},
    }
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 取得函數的結果
        json_data = func(*args, **kwargs)
        # 生成 JSON Schema
        return infer_schema(json_data)

    return wrapper
