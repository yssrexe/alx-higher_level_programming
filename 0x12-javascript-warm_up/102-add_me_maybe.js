#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const newVal = number + 1;
  theFunction(newVal);
};
