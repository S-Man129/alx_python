#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

# Check if a letter argument is provided, default to empty string if not
if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

# URL and data to be sent in the POST request
url = "http://0.0.0.0:5000/search_user"
data = {'q': letter}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Check for request success

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print("Request error:", e)
