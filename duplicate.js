/**
 * @param {number[]} nums
 * @return {boolean}
 * https://leetcode.com/problems/contains-duplicate/
 * https://dev.to/will_devs/javascript-how-to-check-if-an-array-has-duplicate-values-cha
 */
var containsDuplicate = function(nums) {
    // create a new set (Set objects are collections of values)
    const numbers = new Set();
    // loop over the array 
    for (let num of nums) {
        // if the numbers does not have that num, 
        if(!numbers.has(num)) {
            // add it to numbers.
            numbers.add(num);
        // otherwise return true as the number is a duplicate
        } else {
            return true;
        }
    }
    // once loop is complete if there are no duplicates return false
    return false;
};


// Given an array of intgers, find if the array contains duplicates. If there are duplicates return true, otherwise false.
// Loop array
// Create a set
// If item is not the set, add item to the set
// If item is in the set, return true
// If all items are looped and no items match what is in the set, return false


var containsDuplicate = function(nums) {
    return new Set(nums).size !== nums.length
};

function containsDuplicate(nums) {
    const numbers = []

    for (let i = 0; i < array.length; i++) {
        let value = array[i]
        if (valuesAlreadySeen.indexOf(value) !== -1) {
            return true
        }
        valuesAlreadySeen.push(value)
    }
    return false
}