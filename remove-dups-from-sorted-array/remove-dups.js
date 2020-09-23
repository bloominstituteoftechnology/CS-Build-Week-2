var removeDuplicates = function(nums) {       
  let start = nums[0];
  console.log('start', start)
  for (let i = [1]; i < nums.length; i++) {
      if (nums[i] === start) {
          console.log('NUMS-I', nums[i])
          nums.splice(i, 1);
          --i;
      }
      start = nums[i];
  }
  return nums.length;
};
