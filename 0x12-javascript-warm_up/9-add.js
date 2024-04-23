#!/usr/bin/node
const args = require('process').argv;
const num1 = parseInt(args[2], 10);
const num2 = parseInt(args[3], 10);
function add (a, b) {
  return a + b;
}

console.log(add(num1, num2));
