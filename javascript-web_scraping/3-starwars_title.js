#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
