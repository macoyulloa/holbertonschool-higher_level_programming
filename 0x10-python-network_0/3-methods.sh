#!/bin/bash
# DELETE request to the URL
curl -sI $1 | grep Allow: | cu t -b 8-
