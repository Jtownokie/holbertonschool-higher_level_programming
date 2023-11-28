#!/usr/bin/node

exports.converter = function (base) {
  if (base === 10) {
    function printBaseTen (num) {
      return (num);
    }
    return (printBaseTen);
  } else {
    function printOther (num) {
      return (num.toString(base));
    }
    return (printOther);
  }
};
