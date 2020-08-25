/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // understand: there are two linked lists. each node of the linked list represents a digit in a number
    // add the numbers that these two linked lists represent, and return the result as a linked list
    // in the same format (reversed)
    // plan
    // first, figure out the digit that each linked list represents by iterating through the values at each node
    // and putting those values into a variable

    function getNums(ll){
        num = ''
        while(ll.next){
            num += ll.val
            ll = ll.next
        }
        num+= ll.val
        return(num.split('').reverse().join(''))
    }
    
    // then, add the two digits
    
    let vals = String(BigInt(getNums(l1)) + BigInt(getNums(l2))).split('')
    
    // then, split the digits and create a linked list out of them
    
    let i = 0
    let held
    while(i < vals.length){
        held = new ListNode(vals[i], held)
        i += 1
    }
    
    return(held)
    
};