#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  for (let index = 0; index < list.length; index++) {
    if (searchElement === list[index]) {
      j++;
    }
  }
  return j;
};
