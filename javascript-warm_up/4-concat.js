#!/usr/bin/node
import { argv } from 'node:process';

const firstArg = argv[2];
const secondArg = argv[3];

console.log(firstArg + ' is ' + secondArg);
