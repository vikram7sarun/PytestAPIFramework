# utils/schema_validator.py
from jsonschema import validate

def validate_json_schema(response, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)
    validate(instance=response.json(), schema=schema)
