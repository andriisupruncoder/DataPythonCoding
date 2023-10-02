import requests_html

# Create a session object
session = requests_html.HTMLSession()

# Make a request to a web page
response = session.get("https://www.example.com")

# Extract the title of the page
title = response.html.find("title").text

# Print the title
print(title)