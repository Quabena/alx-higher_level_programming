#!/usr/bin/node

// Import the 'fs' module
const fs = require('fs');

// Get the file path and the string to write from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file asynchronously with utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if writing fails
    console.log(err);
  }
});
