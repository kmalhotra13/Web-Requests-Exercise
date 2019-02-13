# challenge 3

# Write a Python program which issues a GET request for this gradebook.json data, then calculate and print the average, min, and max grades.
# https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json

# GOAL: Calculate the average grade from the link

import json
import requests

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json"
response = requests.get(request_url)

print(response.status_code)
print(type(response.status_code))

print(response.text)
print(type(response))

# response_text = response.text

# parsed_response = json.loads(response_text)

# print(parsed_response)
# print(type(parsed_response))

# print("The name of the product is: " + parsed_response["name"])