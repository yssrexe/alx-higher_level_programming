#!/usr/bin/python3
"""
Python script that fetches
"""

import requests

data = requests.get("https://alx-intranet.hbtn.io/status")

print("Body response:")
print(f"\t- type: {type(data.text)}")
print(f"\t- content: {data}")
