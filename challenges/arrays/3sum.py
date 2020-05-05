'''
first solution using hashtables

#dictionary to store differences
	#dictionary to store sums of two values 
	
	#for each i in array: 
		#difference = target - element
		#diff[difference] = element
		
		#for j in range(i, len(array)): 
			#sum = first + element
			
			#if sum not in sums: 
				#sums[sum] = [[i, j]]
				
			#else: 
				#sums[sum].append([i, j])
	
	
    
this resulted in duplicate triplets and took a lot of extra time and space


triplets = []
	
	#for each i in array:
for i in range(0, len(arr)): 
	difference = 0 - arr[i]
	diff[difference] = arr[i]
		
	for j in range(i+1, len(arr)): 
		sum = arr[i] + arr[j]
			
		if sum not in sums: 
			sums[sum] = [[arr[i], arr[j]]]
				
		else: 
			sums[sum].append([arr[i], arr[j]])

for j in diff: 
  if j in sums: 
    
    triplets.extend(sums[j])
      

print(diff)
print(sums)


better solution

def threeNumberSum(array, targetSum):
    #create an array to store triplets
	#sort the given array in ascending order 
	#create a variable to sum of three elements 
	
	#for i in range(0, len(array) -2 ) #-2 because right will point to last  
		#create a variable to point to the element after current elements
		#right = len(array) - 1
		#while left < right:  
			#current_sum = array[i] + array[left] + array[right]
			#if current_sum == targetSum: 
				#triplets.append([array[i], array[left], array[right]])
				#left += 1
				#right -= 1

			#elif current_sum > targetSum: 
				#right -= 1
			#elif current_sum < targetSum: 
				#left += 1

	
'''


def threeSum(nums, target):
    nums.sort()
    triplets = []
        
    for i in range(len(nums) - 2): 
            left = i + 1
            right = len(nums) - 1
            current_sum = nums[i] + nums[left] + nums[right]
            while right > left: 
                if current_sum == 0: 
                    left += 1
                    right -= 1
                    triplets.append([nums[i], nums[left], nums[right]])
                elif current_sum > 0: 
                    right -= 1
                elif current_sum < 0: 
                    left += 1
                    
    return triplets

print(threeSum([-1, 0, 1, 2, -1, -4]))