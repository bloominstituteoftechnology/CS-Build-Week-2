class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        '''
        U: find out if an array has any duplicate values
        if there is at least one duplicate value return true
        means we do not have to iterate through the entire array
        
        P: 
        
        As soon as the function finds a duplicate return true
        
        #1: 
            use the built in sort method on the list
            compare two elements until we reach the end 
        
        #2: 
            use a hash table to keep track of duplicates 
            
            iterate through the list 
            
            if key for value does not exist, create one
            
            if key does exist, return true
        
        '''
        
        nums_dict = dict()
        
        for i in range(0, len(nums)): 
            if nums[i] in nums_dict: 
                return True
            else: 
                nums_dict[nums[i]] = i
           
        return False