#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""

import sys
import requests

if __name__ == "__main__":
    arv = sys.argv
    urs = requests.get(arv[1])
    data = urs.headers.get("X-Request-Id")
    print(data)
