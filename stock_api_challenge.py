# Stock Price Challenge

# goal: print the latest closing price

import json
import os
import requests


api_key = os.environ.get(alphavantage_api_key)
print(api_key)

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=_____________"

response = requests.get(request_url)

print("RESPONSE STATUS: " + str(response.status_code))
print("RESPONSE TEXT: " + response.text)

parsed_response = json.loads(response.text)

print("THE LATEST CLOSING PRICE IS: $XYZ.00")
print("THE AVERAGE GRADE IS: " + str(avg_grade))