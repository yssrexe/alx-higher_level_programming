#!/usr/bin/node

const file = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

fs.writeFile(file, text, 'utf-8', (err) => {
  if (err) {
    console.error(`${err.message}`);
  }
});
