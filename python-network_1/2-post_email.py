#!/usr/bin/python3
"""
Python script to send POST request to given URL with given email as parameter
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Check for request success

    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
