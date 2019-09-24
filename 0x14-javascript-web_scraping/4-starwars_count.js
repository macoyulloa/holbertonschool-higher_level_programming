#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const listAll = JSON.parse(body).results;
    const listPerson = listAll.map(listEach => listEach.characters);
    const flatList = listPerson.reduce((acc, it) => [...acc, ...it]);
    const count = flatList.filter(each => each.includes('/18/')).length;
    console.log(count);
  }
});
