#!/usr/bin/node
import { argv } from 'node:process';

const scriptArg = argv[2];

if (scriptArg) {
  console.log(scriptArg);
} else {
  console.log('No argument');
}
