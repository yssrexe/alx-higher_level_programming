#!/usr/bin/node
const args = require('process').argv;

const size = parseInt(args[2], 10);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < args[2]; index++) {
    console.log('X'.repeat(args[2]));
  }
}
