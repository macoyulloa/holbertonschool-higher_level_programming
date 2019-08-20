#!/bin/bash
# Send a JSON POST
curl -sd "@$2" -H "Content-Type: application/json" -X "POST" "$1"
