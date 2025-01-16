#!/bin/bash
# This script sends a GET request to the URL passed as the first argument and displays the body of the response if the status code is 200
curl -s -L "$1" -o response.txt
if [ "$(head -n 1 response.txt | cut -d' ' -f1)" == "HTTP/1.1" ] && [ "$(head -n 1 response.txt | cut -d' ' -f2)" == "200" ]; then
  tail -n +2 response.txt
fi

