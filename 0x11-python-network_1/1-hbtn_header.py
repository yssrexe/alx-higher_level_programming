#!/usr/bin/python3

import urllib.request
import sys

arv =  sys.argv
with urllib.request.urlopen(arv[1]) as rep:
    data = rep.headers["X-Request-Id"]
print(data)
