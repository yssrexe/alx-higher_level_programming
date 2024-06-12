#!/usr/bin/python3

import requests
import notify2
from time import sleep

notify2.init('vk')

n = notify2.Notification("1337", "1337 is UP.")

url = "https://admission.1337.ma/en/candidature/piscine"


while True:
    data = requests.get(url)
    print(data.status_code)
    if data.status_code in range(200, 300):
        n.show()
    sleep(3)
