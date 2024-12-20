#!/usr/bin/node
/**
 * A square class that inherits from the previous square class
 */

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
