#!/bin/bash
# The script takes in a URL as an argument, sends a GET request with a custom header, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"

