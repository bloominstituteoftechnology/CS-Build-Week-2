/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // init indices
//     ans = []
    
//     while (!ans.length){
//         for(let i = 0; i < nums.length; i++){
//             for(let j = i + 1; j < nums.length; j++){
//                 if(nums[i] + nums[j] === target){
//                     ans = [i, j]
//                 }
//             }
            
//         }
//     }
//     return(ans)
    
    
    // return the indices of two numbers that add up to the target
    
    // create a lookup table, key is the item, value is its index
    
    // in the loop for creating the table, check if the complement is in the table
    
    let comps = {}
    
    for(let i = 0; i < nums.length; i++){
        comp = target - nums[i]
        if (comp in comps){
            return([i, comps[comp]])
        }
        comps[nums[i]] = i
    }
    
}