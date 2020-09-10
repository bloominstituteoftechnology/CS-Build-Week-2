class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # create a set b/c sets can't have dups
        num_set = set()
        no_dups = -1
        
        # loop through the list
        for i in range(len(nums)):
            # check for number that is repeated
            if nums[i] in num_set:
                # return that number
                return nums[i]
            #. if the number is not repeating 
            else:
                # add it to the set
                num_set.add(nums[i])
                
        return no_dups