#!/usr/bin/node
// Prints first arguement passed to it

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
