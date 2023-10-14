import requests

def get_bmw_description():
    response = requests.get("https://bard.google.com/entity/BMW")
    if response.status_code == 200:
        data = response.json()
        description = data["description"]
        return description
    else:
        raise Exception("Failed to get description")

if __name__ == "__main__":
    description = get_bmw_description()
    print(description)