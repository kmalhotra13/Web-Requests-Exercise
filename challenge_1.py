# challenge_1.py

# Write a Python program which issues a GET request for this product.json data, then print the product's "name".
# https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products/1.json
# GOAL: get the product name

import json
import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products/1.json"
response = requests.get(request_url)

# print(response.status_code)
# print(type(response.status_code))

# print(response.text)
# print(type(response))

response_text = response.text

parsed_response = json.loads(response_text)

# print(parsed_response)
# print(type(parsed_response))

print("The name of the product is: " + parsed_response["name"])