#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display
your id.
"""

import requests
import sys

if __name__ == "__main__":
    # Retrieving GitHub username and PAT from argument
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for the authenticated user
    url = "https://api.github.com/user"

    try:
        # Performing a GET request with Basic Authentication
        response = requests.get(url, auth=(username, token))

        # Checking if response indicates a successful authentication
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        else:
            print("None")
    except Exception as e:
        # Print 'None' for any errors
        print("None")
