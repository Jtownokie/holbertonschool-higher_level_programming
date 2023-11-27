#!/usr/bin/node
const argv = process.argv;

const numArg = Math.floor(Number(argv[2]));

if (numArg) {
  console.log(`My number: ${numArg}`);
} else {
  console.log('Not a number');
}
