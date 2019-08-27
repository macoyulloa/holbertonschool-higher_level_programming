#!/usr/bin/python3
" using a urllib library "
import urllib.request
from sys import argv

if __name__ == "__main__":
    " display a header variable "
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
