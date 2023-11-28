#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numFound = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numFound += 1;
    }
  }
  return (numFound);
};
