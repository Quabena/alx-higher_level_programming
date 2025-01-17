#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter, and
finally displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Retrieving the URL and email from the cmd-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Creating the payload for the POST request
    payload = {'email': email}

    # Sending the POST request to the URL with the email parameter
    response = requests.post(url, data=payload)

    # Displaying/Printing the response body
    print(response.text)
