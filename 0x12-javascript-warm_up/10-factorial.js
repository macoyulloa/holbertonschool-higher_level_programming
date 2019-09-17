#!/usr/bin/node
function factorial (a) {
  if (a > 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

const val1 = parseInt(process.argv[2]);
const x = factorial(val1);
console.log(x);
