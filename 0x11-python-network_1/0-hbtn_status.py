#!/usr/bin/python3

"""
This script fetches the URL https://alx-intranet.hbtn.io/status
and display the body of the response, using urllib package.
"""

import urllib.request

if __name__ == "__main__":
    # The URL to be fetched
    url = "https://alx-intranet.hbtn.io/status"

    # Using 'with' statement to hadnle the request
    with urllib.request.urlopen(url) as response:
        # Reading the body
        body = response.read()

        # Decoding the body
        decoded_body = body.decode('utf-8')

        # Printing/Displaying the result
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {decoded_body}")
