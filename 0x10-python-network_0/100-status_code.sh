#!/bin/bash
# Display the status code response 
curl -sI $1 | grep HTTP/1.0 | cut -d " " -f2
