#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  process.argv.forEach((val) => {
    console.log(`${val}`);
  });
}
