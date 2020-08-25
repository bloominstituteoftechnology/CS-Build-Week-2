/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // Understand: If an array contains more than one instance of the same item, return true
    // else, return false
    // Plan: 
    // iterate through the array
    // check each number against every following number
    // if there's a match, return true
    // initial execution:
    // let ans = false
    // nums.forEach((num, index) => {
    //     if(nums.slice(index + 1, nums.length).includes(num)){
    //         ans = true
    //     }
    // })
    // return(ans)
    // Reflect naive: this was too slow to handle large inputs
    // We need a data structure that has faster lookups (hash table?)
    // New plan: start with an empty object
    // iterate through the array
    // if the current item is in the object, break out of the iteration and return true
    // return false
    // New execution:
    // let vals = {}
    // let ans = false
    // nums.forEach(num => num in vals ? ans = true : vals[num] = '')
    // return(ans)
    // New reflection: This works with large inputs but uses more memory and takes longer than other possible solutions
    // I never wrote the code to break out of the loop.
    // New plan: add the break
    // forEach doesn't accept a break, so we'll have to use another method
    // let ans = false
    // let vals = {}
    // for(let i = 0; i<nums.length; i++){
    //     if(nums[i] in vals){
    //         ans = true
    //         break
    //     } else{
    //         vals[nums[i]] = ''
    //     }
    // }
    // return(ans)
    // New reflection: final implementation is significantly faster than previous ones, but still takes up quite a bit of memory and is still slower than 33% of other solutions.
// There's probably a way to speed this up even further but it's escaping me
// Possibly sort first? That wouldn't necessarily add to big O.
// Sorting in general and checking if the value is right next to it?
    // After sorting, it's now slower....
    // JS set doesn't allow for duplicates
    const noDupes = [...new Set(nums)]
    // console.log([...noDupes])
    // sets don't have a length property, so we'll have to put it back into an array after converting to a set
    if(noDupes.length === nums.length){
        return(false)
    } else {
        return(true)
    }
    // reflection: This is now much faster and takes up a bit less space. we might be able to reduce the amount of space by playing some code golf
    // if([...new Set(nums)].length === nums.length){
    //     return(false)
    // } else{
    //     return(true)
    // }
    // reflection: this somewhat reduced the amount of space, but increased the amount of time for some reason?
    // further reflection: the runtime varies wildly???
};
