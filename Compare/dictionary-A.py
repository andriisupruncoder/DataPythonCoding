import json

cell_value = """{"key1": "value1", "key2": "value2"}"""

dictionary = json.loads(cell_value)

print(dictionary)