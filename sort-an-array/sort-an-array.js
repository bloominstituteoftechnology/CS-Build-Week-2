var sortArray = function(nums) {
  // check for valid input
  if (nums.length <= 1) return nums
  // create pivot point and pop number from there in array
  const pivot = nums.pop();
  // create new array to store numbers smaller than pivot
  const smlArr = sortArray(nums.filter(n => n <= pivot));
  // create new array to store numbers larger than pivot
  const lrgArr = sortArray(nums.filter(n => n > pivot));
  // return new array by combining two new arrays divided by the pivot point
  return smlArr.concat(pivot, lrgArr)
};