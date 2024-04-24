#!/usr/bin/node
const { list } = require('./100-data');
const doublelist = list.map((x, i) => x * i);

console.log(list);
console.log(doublelist);
