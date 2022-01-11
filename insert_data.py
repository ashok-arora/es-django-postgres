import requests
import json

url = "http://127.0.0.1:8080/api/images"
url_1 = "https://random-data-api.com/api/food/random_food"
url_2 = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"

for _ in range(10):
    response_1 = requests.request("GET", url_1).json()
    response_2 = requests.request("GET", url_2).json()

    payload = json.dumps(
        {
            "name": response_1["dish"],
            "description": response_1["description"],
            "image_url": response_2["url"],
        }
    )
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
