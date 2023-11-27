#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  return (a + b);
}
const callAdd = add(Number(argv[2]), Number(argv[3]));

console.log(callAdd);
