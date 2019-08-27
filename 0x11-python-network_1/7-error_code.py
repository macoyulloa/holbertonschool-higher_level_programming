#!/usr/bin/python3
" using a urllib library "
import requests
from sys import argv

if __name__ == "__main__":
    " managing errors "
    url = argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        print(req.text)
    else:
        print("Error code:", req.status_code)
