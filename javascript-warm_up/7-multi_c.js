#!/usr/bin/node
const argv = process.argv;

const numTimes = Number(argv[2]);

if (numTimes) {
  for (let i = 0; i < numTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
