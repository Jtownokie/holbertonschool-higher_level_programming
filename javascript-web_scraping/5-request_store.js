#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;

request(`${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(`${argv[3]}`, `${body}`, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
