#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const listAll = JSON.parse(body);
    const listTask = listAll.filter(it => it.completed);
    const groupByCompleted = listTask.reduce((acc, it) => {
      acc[it.userId] = acc[it.userId] + 1 || 1;
      return acc;
    }, {});
    console.log(groupByCompleted);
  }
});
