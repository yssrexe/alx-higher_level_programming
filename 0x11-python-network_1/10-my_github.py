#!/usr/bin/python3
"""
    a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    url = f"https://api.github.com/users/{args[1]}"
    headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        "Authorization": f"Bearer {args[2]}",
        "Accept": "application/vnd.github+json"
    }
    res = requests.get(url, headers=headers)
    data = res.json()

    print(data.get('id'))
