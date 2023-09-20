#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = "https://api.github.com/user"

try:
    response = requests.get(url, auth=(username, personal_access_token))
    response.raise_for_status()  # Check for request success

    user_data = response.json()
    user_id = user_data.get('id')

    if user_id:
        print(f"Your GitHub ID is: {user_id}")
    else:
        print("Unable to retrieve GitHub ID from the response")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

except ValueError as e:
    print("Failed to parse JSON response:", e)