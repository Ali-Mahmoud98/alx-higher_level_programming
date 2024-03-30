#!/usr/bin/node
// const request = require('request');
// const url = 'https://swapi.co/api/films/' + process.argv[2];
// request(url, function (error, response, body) {
//   if (!error) {
//     const characters = JSON.parse(body).characters;
//     characters.forEach((character) => {
//       request(character, function (error, response, body) {
//         if (!error) {
//           console.log(JSON.parse(body).name);
//         }
//       });
//     });
//   }
// });

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
