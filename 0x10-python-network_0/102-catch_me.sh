#!/bin/bash
# A script that makes a request to 0.0.0.0:5000/catch_me to get "You got me!" in the response body
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
