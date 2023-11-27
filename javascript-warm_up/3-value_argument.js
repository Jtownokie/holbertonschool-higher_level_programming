#!/usr/bin/node
const argv = process.argv;

const scriptArg = argv[2];

if (scriptArg) {
  console.log(scriptArg);
} else {
  console.log('No argument');
}
