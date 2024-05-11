#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to the URL
"""

import sys
import requests

if __name__ == "__main__":
    arv = sys.argv
    try:
        urlerror = requests.get(arv[1])
        urlerror.raise_for_status()
        print(urlerror.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
