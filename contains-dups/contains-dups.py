/*
 * @param {number[]} nums
 * @return {boolean}
 */
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 

    # First pass solution not very efficient
    checked = set()
        
        for number in nums:
            if number in checked:
                return True
            checked.add(number)
        return False 



  # Single line solution, slightly more efficient
  # return len(set(nums)) < len(nums)