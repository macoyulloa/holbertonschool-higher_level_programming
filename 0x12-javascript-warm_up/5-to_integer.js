#!/usr/bin/node
const val = process.argv[2];
if (Number(val)) {
  console.log('My number: ' + val);
} else {
  console.log('Not a number');
}
