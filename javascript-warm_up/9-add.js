#!/usr/bin/node
import { argv } from 'node:process';

function add (a, b) {
  return (a + b);
}
const callAdd = add(Number(argv[2]), Number(argv[3]));

console.log(callAdd);
