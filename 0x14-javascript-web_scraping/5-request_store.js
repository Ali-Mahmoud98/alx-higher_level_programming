#!/usr/bin/node

// const request = require('request');
// const fs = require('fs');
// const url = process.argv[2];
// const filePath = process.argv[3];

// request(url, function (err, response, body) {
//   if (err) {
//     console.log(err);
//   } else {
//     fs.writeFile(filePath, body, 'utf-8');
//   }
// });

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
