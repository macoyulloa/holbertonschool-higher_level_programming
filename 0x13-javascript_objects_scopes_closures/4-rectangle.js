#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const copyH = this.height;
    this.height = this.width;
    this.width = copyH;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
