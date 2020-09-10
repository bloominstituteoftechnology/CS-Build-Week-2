class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sanity checks, parameters are positive integers between 0 and 5001
        if len(nums) > 5000 and len(nums) < 1:
            return []        
        
        start = 0
        end = len(nums) - 1
        # as the testcases are smaller arrays use quicksort
        self.quickSort(nums, start, end)
        return nums 
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return
        
        # find mid index for pivot point
        md_index = (start + end) // 2
        # swap first and mid index elements
        nums[start], nums[md_index] = nums[md_index], nums[start]
        
        p_index = self.partition(nums, start, end)
        # recursive calls to both the left and right sides
        self.quickSort(nums, start, p_index - 1)
        self.quickSort(nums, p_index + 1, end)
    
    def partition(self, nums, start, end):
        
        low = start + 1
        high = end
        pivot = nums[start]
        
        while True:
            
            while low <= high and nums[high] >= pivot:
                high -= 1
                
            while low <= high and nums[low] <= pivot:
                low += 1
                
            if (low <= high):
                nums[low], nums[high] = nums[high], nums[low]
            else:
                break
        # swap start index with high index                
        nums[start], nums[high] = nums[high], nums[start]
        return high