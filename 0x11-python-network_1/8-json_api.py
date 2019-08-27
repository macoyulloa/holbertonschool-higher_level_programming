#!/usr/bin/python3
" using a urllib library "
import requests
from sys import argv

if __name__ == "__main__":
    " POST request, display a body and mail "
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        values = {'q': argv[1]}
    else:
        values = {'q': ""}
    req_post = requests.post(url, data=values)
    try:
        req = req_post.json()
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except:
        print("Not a valid JSON")
