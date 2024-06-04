#!/usr/bin/node
const requested = require('request')
const link = process.argv[2]

requested(link, (data, err, body) => {
    if (err) {
        console.error(`${err.message}`)
    } else {
        console.log(`code : ${data.statusCode}`)
    }
})
