#!/usr/bin/python3
" Fetching a URL "
import requests

if __name__ == "__main__":
    " fetching the URL https://intranet.hbtn.io/status "
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
