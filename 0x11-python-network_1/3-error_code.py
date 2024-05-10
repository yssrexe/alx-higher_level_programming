#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""

import sys
import urllib.request
from urllib.error import HTTPError


def main():
    arv = sys.argv
    try:
        with urllib.request.urlopen(arv[1]) as cos:
            print(cos.read().decode())
    except HTTPError as err:
        print(f"Error code: {err.code}")


if __name__ == "__main__":
    main()
