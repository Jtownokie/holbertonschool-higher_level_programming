#!/usr/bin/node
const { argv } = require('node:process');

const scriptArg = argv[2];

if (scriptArg) {
  console.log(scriptArg);
} else {
  console.log('No argument');
}
