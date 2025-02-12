#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the URL from the first command-line argument
const url = process.argv[2];

// Send a GET request to the URL
request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    // Print the HTTP status code
    console.log(`code: ${response.statusCode}`);
  }
});
