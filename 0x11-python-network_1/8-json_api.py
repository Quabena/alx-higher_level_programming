#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter. The response is processed based on its
content and formatting.
"""

import requests
import sys

if __name__ == "__main__":
    # Getting the letter argument. Empty string if none provided.
    letter = sys.argv[1] if len(sys.argv) >= 2 else""
    payload = {'q': letter}

    try:
        # Sending the POST request to the URL with the letter parameter
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data=payload)

        # Parsing the response body as JSON
        json_data = response.json()

        # Checking if the JSON data is empty
        if not json_data:
            print("No result")
        else:
            # Display the id and name if the JSON has data
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
    except ValueError:
        # Invalid JSON
        print("Not a valid JSON")
