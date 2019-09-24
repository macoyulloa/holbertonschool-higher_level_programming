#!/usr/bin/node
const list = require('./100-data').list;

const map1 = list.map((val, index) => val * index);
console.log(list);
console.log(map1);
