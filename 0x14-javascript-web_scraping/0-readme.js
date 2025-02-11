#!/usr/bin/node

// Import the 'fs' (File System) module to handle file operations
const fs = require('fs');

// Get the file path from the first command-line argument
const filePath = process.argv[2];

// Read the file asynchronously with utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
  // Print the error object if an error occurs
    console.log(err);
  } else {
  // Print the file content if reading is successful
    console.log(data);
  }
});
