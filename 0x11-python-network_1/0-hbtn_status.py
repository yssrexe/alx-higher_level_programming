#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as responce:
    data = responce.read()
    decodedata = data.decode("utf-8")

print("Body response:")
print(f"\t- type: {type(data)}")
print(f"\t- content: {data}")
print(f"\t- utf8 content: {decodedata}")
