#!/usr/bin/node

const arg = process.argv[2];
const fs = require('fs');

fs.readFile(arg, 'utf-8', (err, data) => {
  if (err) {
    console.error(`Error reading file: ${err.message}`);
    process.exit(1);
  }
  console.log(data);
});
