#!/usr/bin/node

exports.converter = function (base) {
  if (base === 10) {
    const printBaseTen = (num) => num;
    return (printBaseTen);
  } else {
    const printOther = (num) => num.toString(base);
    return (printOther);
  }
};
