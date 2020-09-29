/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let start = 0, res = 0;
  let charsInWindow = new Set();
  
  for (let end = 0; end < s.length; end++) {
      let entering = s[end];
      console.log('test', entering)
      
      while (charsInWindow.has(entering)) {
          charsInWindow.delete(s[start++]);
      }
      charsInWindow.add(s[end]);
      console.log('look', s[end])
      res = Math.max(res, end - start + 1);
      console.log(res, end - start + 1)
  }
  return res;
}