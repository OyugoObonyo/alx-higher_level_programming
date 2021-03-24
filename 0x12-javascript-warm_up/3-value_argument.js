#!/usr/bin/node
// Prints first arguement passed to it

const arguements = process.argv;
if (arguements[2]) {
  console.log(arguements[2]);
} else {
  console.log('No arguement');
}
