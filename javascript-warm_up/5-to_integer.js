#!/usr/bin/node
import { argv } from 'node:process';

const numArg = Math.floor(Number(argv[2]));

if (numArg) {
  console.log(`My number: ${numArg}`);
} else {
  console.log('Not a number');
}
