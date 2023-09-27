import json
from jsonschema import validate, ValidationError

# Load the JSON data
with open("user_logs.json", "r") as file:
    data = json.load(file)

# Define the schema
schema = {
    "type": "object",
    "properties": {
        "logs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "string"},
                    "action": {
                        "type": "string",
                        "enum": ["login", "view_product"]
                    },
                    "timestamp": {
                        "type": "string",
                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
                    },
                    "product_id": {"type": "string"}
                },
                "required": ["user_id", "action", "timestamp"],
                "dependencies": {
                    "action": {
                        "oneOf": [
                            {
                                "properties": {
                                    "action": {"enum": ["login"]},
                                    "product_id": {"not": {}}
                                }
                            },
                            {
                                "properties": {
                                    "action": {"enum": ["view_product"]},
                                    "product_id": {}
                                },
                                "required": ["product_id"]
                            }
                        ]
                    }
                }
            }
        }
    },
    "required": ["logs"]
}

# Validate the JSON data against the schema
try:
    validate(instance=data, schema=schema)
    print("The JSON data adheres to the schema.")
except ValidationError as e:
    print(f"Validation error: {e.message}")
