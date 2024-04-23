#!/usr/bin/node
const procces = require('process');

const args = procces.argv;
const arglenth = args.length;

if (arglenth === 2) {
  console.log('No argument');
} else if (arglenth === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
