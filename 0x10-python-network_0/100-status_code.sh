#!/bin/bash
# Display the status code response
 curl -s -o /dev/null -w "%{http_code}" $1 
