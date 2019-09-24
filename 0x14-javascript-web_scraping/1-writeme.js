#!/usr/bin/node

const file = require('fs');
const data = process.argv[3];
file.writeFile(process.argv[2], data, (error) => {
  if (error) { console.log(error); }
});
