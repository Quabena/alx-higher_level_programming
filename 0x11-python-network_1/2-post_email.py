#!/usr/bin/python3

"""
This script takes a URL and an email address, sends a POST request
to the URL with the email as a parameter, then displays the body of
the response.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Retrieving the URL and email from the cmd arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Creating a dictionary with the email parameter
    data = {'email': email}

    # Encoding the data to be sent as part of the POST request
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Sending the POST request using 'with'
    with urllib.request.urlopen(url, data=encoded_data) as response:
        # Reading and encoding the response body
        body = response.read().decode('utf-8')

        # Printing/Displaying the response body
        print(body)
