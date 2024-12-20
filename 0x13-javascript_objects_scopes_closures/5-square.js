#!/usr/bin/node

// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define the Square class
class Square extends Rectangle {
  constructor (size) {
    // Call the parent class constructor with width and height set to size
    super(size, size);
  }
}

module.exports = Square;

