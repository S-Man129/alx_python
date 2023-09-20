#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""

# if __name__ == "__main__":
#     import urllib.request
#     url = "https://intranet.hbtn.io/status"
#     with urllib.request.urlopen(url) as response:
#         body = response.read()
#         print("Body response:")
#         print("\t- type: {}".format(type(body)))
#         print("\t- content: {}".format(body))
#         print("\t- utf8 content: {}".format(body.decode("utf-8")))

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
