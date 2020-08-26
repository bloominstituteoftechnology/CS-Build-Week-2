class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create a hashtable to store key, value pairs
    hashtable = {}
    # store keys as index location and vals as original str
    # loop through hashtable 
    for index, num in enumerate(nums):
      # if you find the index number 
      if num in hashtable:
        # output should show the key, value pair for the one you're looking for
        return [hashtable[num], index]
      # in hashtable subtract num at specified index from given target 
      hashtable[target - num] = index