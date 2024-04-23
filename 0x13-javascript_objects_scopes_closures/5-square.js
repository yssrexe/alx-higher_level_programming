#!/usr/bin/node
const rect = require('./4-rectangle.js');

class Square extends rect {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
