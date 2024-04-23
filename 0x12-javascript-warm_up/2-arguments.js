#!/usr/bin/node
const procces = require('process');

const args = procces.argv;
const arglenth = args.length;

if (arglenth === 1) {
  console.log('No argument');
} else if (arglenth === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
