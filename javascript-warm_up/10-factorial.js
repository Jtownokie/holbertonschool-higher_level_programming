#!/usr/bin/node
const argv = process.argv;

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const result = factorial(Number(argv[2]));

console.log(result);
