#!/usr/bin/node
const val = process.argv[2];
if (Number(val)) {
  for (let i = 0; i < val; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
