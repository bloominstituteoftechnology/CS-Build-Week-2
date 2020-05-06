function threeNumberSum(array, targetSum) {
    array.sort((a, b) => a - b) //forgot about this!
    let triplets = []
  
    for( i = 0; i < array.length - 2; i++){
        let left = i + 1
        let right = array.length - 1
        while (left < right){
            let current_sum = array[i] + array[left] + array[right]
            if (current_sum === targetSum){
                triplets.push([array[i], array[left], array[right]])
                left++ 
                right-- 
            }
            else if (current_sum < targetSum){
                left++ 
            }
            else if (current_sum > targetSum){
                right--
            }
              
        }
    }
      
    return triplets
  }