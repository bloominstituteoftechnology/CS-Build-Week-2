/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // create a set (no duplicates allowed in sets!) from the numbers array
  const set = new Set(nums);

  // if the set is equivalent in length to the nums array, we must not have any duplicates
  if (set.size === nums.length) {
    return false;
  } else {
    return true;
  }
};
