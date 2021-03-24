#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);
let i = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
