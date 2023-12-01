#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(`${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const starWarsFilms = JSON.parse(body).results;
    let numTimes = 0;
    for (const film of starWarsFilms) {
      if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        numTimes += 1;
      }
    }
    console.log(numTimes);
  }
});
