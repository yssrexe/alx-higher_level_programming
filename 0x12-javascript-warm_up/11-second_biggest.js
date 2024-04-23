#!/usr/bin/node
const { argv: args } = require('process');

const len = args.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  let biggest = parseInt(args[2], 10);
  let secBiggest = parseInt(args[3], 10);

  for (let i = 3; i < len; i++) {
    const number = parseInt(args[i], 10);
    if (number > biggest) {
      secBiggest = biggest;
      biggest = number;
    } else if (number < biggest && number > secBiggest) {
      secBiggest = number;
    }
  }
  console.log(secBiggest);
}
