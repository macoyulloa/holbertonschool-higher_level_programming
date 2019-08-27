#!/usr/bin/python3
" Fetching a URL "
import urllib.request

if __name__ == "__main__":
    " fetching the URL https://intranet.hbtn.io/status "
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
