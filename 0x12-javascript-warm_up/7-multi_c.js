#!/usr/bin/node
const args = require('process').argv;
const res = 'C is fun';
for (let index = 0; index < args[2]; index++) {
  console.log(res);
}
