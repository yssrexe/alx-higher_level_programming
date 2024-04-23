#!/usr/bin/node
const lastclass = require('./5-square.js');
class Square extends lastclass {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let index = 0; index < this.width; index++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
