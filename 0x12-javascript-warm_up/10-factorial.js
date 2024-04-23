#!/usr/bin/node
const { argv: args } = require('process');

const number = parseInt(args[2], 10);

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (Number.isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
