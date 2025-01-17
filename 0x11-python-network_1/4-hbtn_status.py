#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using 'request'
and displays the body of the response
"""

import requests

if __name__ == "__main__":
    # Sending a GET request to the URL
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    # Displaying/Printing the response body
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
