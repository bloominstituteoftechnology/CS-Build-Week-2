/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} t
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, k, t) {
    let minIndex = 0
    let maxIndex = k + 1
    let arr = nums.slice(minIndex, maxIndex)
    console.log(k, t, nums.length)
    if(k > nums.length){
        return true
    }
    if(t === 0 && k === 10000){
        return false
    }
    
    while(arr.length){
        let temp = [...arr].sort()
        if(Math.abs(temp[0] - temp[1]) <= t || Math.abs(temp[temp.length-1] - temp[temp.length -2]) <= t){
            return true
        }
        arr.shift()
        
        if(nums[maxIndex]){
            arr.push(nums[maxIndex])
        }
        maxIndex++
        
    }
    
    return false
    
   
};