#!/usr/bin/python3
"""
    a script that takes in a URL, sends a request to the URL and displays
"""
import urllib.request
import sys


def head():
    arv = sys.argv
    with urllib.request.urlopen(arv[1]) as rep:
        data = rep.headers["X-Request-Id"]
    print(data)


if __name__ == "__main__":
    head()
