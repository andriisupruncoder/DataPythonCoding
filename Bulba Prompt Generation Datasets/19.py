import requests

def make_request(url):
  request = requests.Request(method="GET", url=url)
  response = request.send()
  return response.content

# Make an HTTP request to the Django endpoint
response = make_request("http://localhost:8000/api/v1/users/")

# Handle the response from the server
print(response)