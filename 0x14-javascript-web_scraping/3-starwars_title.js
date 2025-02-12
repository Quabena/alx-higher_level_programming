#!/usr/bin/node

// Import the 'request' library for making HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API using the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the Star Wars API
request.get(url, (error, response, body) => {
  // If an error occurred during the request, log it to the console
  if (error) {
    console.log(error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);
    // Print the movie title
    console.log(data.title);
  }
});
