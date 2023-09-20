#!/usr/bin/python3
"""
Python script to send request to given URL
and display body of response, decoded
also handles urllib.error.HTTPError exception
"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for request success

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
