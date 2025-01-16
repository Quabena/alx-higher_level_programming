#!/bin/bash
# The script takes a URL, sends a request to it using curl, and displays the size of the response
curl -s -I "$1" | grep -i "Content-Length" | awk '{print $2}'
