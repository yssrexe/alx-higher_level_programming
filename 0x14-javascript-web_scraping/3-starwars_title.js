#!/usr/bin/node
const request = require('request');
const arg = process.argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + String(arg[2]);

request(url, (err, data, body) => {
  if (err) {
    console.error(`${err.message}`);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
