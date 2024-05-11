#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    res = requests.post(url, value)
    print(res.text)
