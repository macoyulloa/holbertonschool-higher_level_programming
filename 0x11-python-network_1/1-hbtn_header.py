#!/usr/bin/python3
" using a urllib library "
import urllib.request
from sys import argv

if __name__ == "__main__":
    " display a header variable "
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
