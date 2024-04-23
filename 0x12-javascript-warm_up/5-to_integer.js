#!/usr/bin/node
const args = require('process').argv;

const num = parseInt(args[2])
if (Number.isNaN(num)) {
    console.log('Not a number')
} else {
    console.log(`${args[2]}`)
}
