#!/usr/bin/node
const argv = process.argv;

if (argv.length > 3) {
  const argInts = [];
  for (let i = 2; i < argv.length; i++) {
    argInts.push(argv[i]);
  }

  argInts.sort(function (a, b) { return a - b; });
  const secondBiggest = argInts[argInts.length - 2];

  console.log(secondBiggest);
} else {
  console.log('0');
}
