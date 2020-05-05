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

'''