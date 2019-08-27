#!/usr/bin/python3
" using a urllib library "
import urllib.request
from sys import argv

if __name__ == "__main__":
    " POST request, display a body and mail "
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode("utf-8"))
