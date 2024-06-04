#!/usr/bin/node
const requested = require('request');
const lin = require('process').argv[2];

requested(lin, (err, data) => {
  if (err) {
    console.error(`${err.message}`);
  } else {
    console.log(`code: ${data.statusCode}`);
  }
});
