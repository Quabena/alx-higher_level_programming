#!/usr/bin/python3
"""
This script takes URL, sends a request to it, and displays the
value of the 'X-Request-Id' found in the header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Retrieving the URL from the cmd arguments
    url = sys.argv[1]

    # Using 'with' to handle the request
    with urllib.request.urlopen(url) as response:
        # Accessing the headers
        headers = response.headers

        # Retrieving the value of 'X-Request-Id' from the headers
        x_request_id = headers.get("X-Request-Id")

        # Printing the value of 'X-Request-Id'
        print(x_request_id)
