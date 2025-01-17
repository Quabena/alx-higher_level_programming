#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the value of the variable 'X-Request-Id' in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Retrieving the URL from the cmd-line arguments
    url = sys.argv[1]

    # Sending a GET request to the URL
    response = requests.get(url)

    # Extracting 'X-Request-Id' from the response headers
    x_request_id = response.headers.get('X-Request-Id')

    # Displaying/Printing the value of 'X-Request-Id'
    print(x_request_id)
