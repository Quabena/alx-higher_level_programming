#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from the first command-line argument
const movieId = process.argv[2];

// Construct the API URL using the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);
    // Print the movie title
    console.log(data.title);
  }
});
