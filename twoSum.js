/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// naive solution
var twoSum = function (nums, target) {
  // iterate over all possible combinations
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      // add & compare to target, making sure nums aren't the same
      if (nums[i] + nums[j] === target && i !== j) {
        return [i, j];
      }
    }
  }
};

// hashtable solution
var twoSum = function (nums, target) {
  const hashtable = {};

  // populate hashtable w/ nums & corresponding indexes
  nums.forEach((num, idx) => (hashtable[num] = idx));

  // iterate nums and attempt to find remainder in hashtable
  for (let i = 0; i < nums.length; i++) {
    const remaining = target - nums[i];
    const remainderIndex = hashtable[remaining];

    if (remainderIndex && remainderIndex !== i) {
      return [i, remainderIndex];
    }
  }
};
