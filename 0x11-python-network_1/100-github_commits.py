#!/usr/bin/python3
"""
This script lists the 10 most recent commits from a given GitHub repository.

Usage:
    ./100-github_commits.py <repository_name> <repository_owner>

Arguments:
    repository_name: The name of the GitHub repository (e.g., 'rails').
    repository_owner: The owner of the repository (e.g., 'rails').

Output:
    Prints the 10 most recent commits in the format:
        <sha>: <author name>
    If there are fewer than 10 commits, prints all available commits.

Requirements:
    - The script uses the GitHub API.
    - No authentication is required for this task.
    - Rate-limited to 60 requests per hour for unauthenticated requests.
"""
import sys
import requests

if __name__ == "__main__":
    # Retrieving the API URL from arguments
    repo_owner = sys.argv[2]  # Second argument: repository owner
    repo_name = sys.argv[1]   # First argument: repository name
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    # Sending a GET request to fetch the commit data from the GitHub API
    response = requests.get(url)

    # Parsing the JSON response into a Python dictionary
    commits = response.json()

    try:
        # Looping through the first 10 commits in the list
        for i in range(10):
            # Extracting and print the SHA and author's name for each commit
            sha = commits[i].get("sha")  # Commit hash (SHA)
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
