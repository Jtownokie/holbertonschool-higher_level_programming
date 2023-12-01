#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(`${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const objectArray = JSON.parse(body);
    const countPerID = {};

    objectArray.forEach(obj => {
      if (obj.completed) {
        if (countPerID[obj.userId]) {
          countPerID[obj.userId]++;
        } else {
          countPerID[obj.userId] = 1;
        }
      }
    });
    console.log(countPerID);
  }
});
