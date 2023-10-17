import json

def string_to_dict(string):
  # Convert the string to a dictionary.
  dictionary = json.loads(string)

  # Return the dictionary.
  return dictionary

# Get the string encapsulated dictionary.
string_dictionary = "{\"key1\": \"value1\", \"key2\": \"value2\"}"

# Convert the string encapsulated dictionary to a dictionary.
dictionary = string_to_dict(string_dictionary)

# Print the dictionary.
print(dictionary)