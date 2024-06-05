#!/usr/bin/node
const request = require('request')
const link = process.argv[2]
const file = process.argv[3]
const fs = require('fs')


request(link, (err, data) => {
    if (err) {
        console.log(err)
    } else {
        fs.writeFile(file, data.body, 'utf-8', (err) => {
            if (err) {
                console.log(err)
            }
        })
    }
})
