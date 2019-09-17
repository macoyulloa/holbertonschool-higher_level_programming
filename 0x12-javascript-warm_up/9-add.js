#!/usr/bin/node
const val1 = parseInt(process.argv[2]);
const val2 = parseInt(process.argv[3]);
let x = add(val1, val2);

function add(a, b){
    console.log(a + b);
}
