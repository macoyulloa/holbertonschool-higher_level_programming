#!/bin/bash
# POST request to the passed URL 
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
