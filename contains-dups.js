/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // create a set
  let numbers = new Set();
  // iterate over the array
  for (let num of nums) {
    // get to a number, check if it's already in the set
    if (!numbers.has(num)) {
      // if it's not in the set add the number to the set
      numbers.add(num);
      // but if you see it was already added to the set
    } else {
      // signal the array contains duplicates
      return true;
    }
  }
  // if code runs and no duplicates are found, return false
  return false;
};
