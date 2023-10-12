import requests
import json

def get_token_value(url):
  # Get the response from the URL.
  response = requests.get(url)

  # Get the JSON data from the response.
  data = json.loads(response.content)

  # Get the token value from the JSON data.
  token_value = data["token"]

  # Return the token value.
  return token_value

# Get the token value from the URL.
token_value = get_token_value("https://example.com/")

# Print the token value.
print(token_value)