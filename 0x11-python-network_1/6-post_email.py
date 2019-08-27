#!/usr/bin/python3
" using a urllib library "
import requests
from sys import argv

if __name__ == "__main__":
    " POST request, display a body and mail "
    values = {'email': argv[2]}
    req_post = requests.post(argv[1], data=values)
    print(req_post.text)
