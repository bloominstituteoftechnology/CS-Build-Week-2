/*

https://leetcode.com/problems/two-sum/



*/



/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    /***************************************************/
    /*  Begin first version                            */
    /***************************************************/
    let diffObj = {}
    let numsLen = nums.length
    
    for (index=0; index<numsLen; index++) {
        let diff = target - nums[index]
        if (diffObj.hasOwnProperty(diff)) {
            return [index,diffObj[diff]]
        }
        else {
            diffObj[nums[index]] = index
        }
    }
    /***************************************************/
    /*  End first version                            */
    /***************************************************/
    
    /***************************************************/
    /*  Begin second version                            */
    /***************************************************/
    // let numsLen = nums.length
    // for (i=0; i<numsLen; i++) {
    //     for(j=0; j<numsLen; j++) {
    //         if ((i !== j) && (nums[i] + nums[j] === target)) {
    //             return [i,j]
    //         }
    //     }
    // }
    /***************************************************/
    /*  End second version                            */
    /***************************************************/
    
    
};
