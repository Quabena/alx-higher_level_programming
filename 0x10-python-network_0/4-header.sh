#!/bin/bash
# The script takes in a URL as an argument, sends a GET request with a custom header.
curl -s -H "X-School-User-Id: 98" "$1"
