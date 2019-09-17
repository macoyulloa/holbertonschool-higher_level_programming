#!/usr/bin/node
const val1 = parseInt(process.argv[2]);
const val2 = parseInt(process.argv[3]);
const x = add(val1, val2);
console.log(x);

function add (a, b) {
  return a + b;
}
