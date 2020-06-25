/**
 * @param {number[]} nums
 * @return {number[]}
 */
const runningSum = function (nums) {
  let sum = 0;
  let result = [];

  function solve() {
    nums.forEach((num) => {
      sum += num;
      result.push(sum);
    });
    return result;
  }

  return solve();
};

const nums = [1, 2, 3, 4];
console.log(runningSum(nums));
