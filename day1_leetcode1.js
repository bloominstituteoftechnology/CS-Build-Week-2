/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    count_of_numbers = {}
    
    for (x of nums) {
        if (count_of_numbers.hasOwnProperty(x)) {
            return true
        }
        else {
            count_of_numbers[x] = 1
        }
    }
    
    return false
};
