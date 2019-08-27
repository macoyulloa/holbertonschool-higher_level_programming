#!/usr/bin/python3
" using a urllib library "
import requests
from sys import argv

if __name__ == "__main__":
    " display a header variable "
    req = requests.get(argv[1])
    print(req.headers.get("X-Request-Id"))
