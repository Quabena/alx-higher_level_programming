#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL and displays
the body of the response, while also handling HTTPError exceptions
by displaying the error codes
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Retrieving the URL from the command-line
    url = sys.argv[1]

    try:
        # Sending the request using 'with' statement
        with urllib.request.urlopen(url) as response:
            # Reading and decoding the response body
            body = response.read().decode('utf-8')

            # Printing/Displaying the response body
            print(body)

    except urllib.error.HTTPError as e:
        # Printing error code
        print(f"Error code: {e.code}")
