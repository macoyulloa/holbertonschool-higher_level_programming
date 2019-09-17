#!/usr/bin/node
const val = process.argv[2];
if (Number(val)) {
  for (let i = 0; i < val; i++) {
    console.log('X'.repeat(val));
  }
} else {
  console.log('Missing size');
}
