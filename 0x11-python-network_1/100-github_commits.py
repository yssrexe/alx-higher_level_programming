#!/usr/bin/python3
"""
    a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    params = f"{args[2]}/{args[1]}/commits?per_page=10"
    url = f"https://api.github.com/repos/{params}"
    res = requests.get(url)
    commits = res.json()
    for commit in commits:
        print(f"{commit.get('sha')}: "
              f"{commit.get('commit').get('author').get('name')}")
