/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  // quickly check if negative 
  if (x < 0) {
      // if yes, return false
      return false
  }
  // check if x is the same as it's reversed form
  return x === reversedInteger(x);
  
};
  // 
  var reversedInteger = function(x) {
      // initialize variable starting as 0
      let reversed = 0;
      // checking if you have positive integer
      while (x > 0) {
          // variable started as 0, * 10 is 0 then add next int of x % 10
          reversed = (reversed * 10) + (x % 10);
          // remove last number of given input
          x = Math.floor(x / 10);
      }
      return reversed;
};