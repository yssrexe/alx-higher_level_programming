#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    url = f"http://0.0.0.0:5000/search_user"
    value = ""
    if len(args) >= 2:
        value = args[1]
    try:
        res = requests.post(url, {"q": value})
        user = res.json()
        if len(user) == 0:
            print("No result")
        else:
            print(f"{[user['id']]} {user['name']}")
    except ValueError as e:
        print("Not a valid JSON")
