#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(`${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(`code: ${response.statusCode}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
