#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""
import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
else:
    print("Error: Unable to fetch URL. Status code:", response.status_code)
