#!/usr/bin/python3
"""
This script lists the 10 most recent commits of a repository
owned by a specified user, using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    # GEtting repository name and owner from cmd-line argument
    repo_name = argv[1]
    owner_name = sys.argv[2]

    # GitHub API url for the commits endpoint
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        # Sending a GET request to the API
        response = requests.get(url)
        # Raising an error for HTTP codes >= 400
        response.raise_for_status()

        # Parsing the JSON response
        commits = reponse.json()

        # Printing/Displaying the 10 most recent commits
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    except requests.exceptions.RequestException as e:
        # HTTP or connection-related errors
        print(f"Error: {e}")
