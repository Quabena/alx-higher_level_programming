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
    url = f"https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name)

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
