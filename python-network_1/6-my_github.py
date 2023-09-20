#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth as Basic_auth
    from sys import argv
    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=Basic_auth(argv[1], argv[2]))
        json_string = response.json()
        print(json_string['id'])
    except Exception as err:
        print("None")