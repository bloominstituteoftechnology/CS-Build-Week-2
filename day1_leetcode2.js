/*


https://leetcode.com/problems/add-two-numbers/


*/



/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    
    /***************************************************************/
    /*    Begin version 1 code                                     */
    /***************************************************************/
    
//     let ll2num = function(ll) {
//         currentNode = ll
//         num = 0n
//         digitValue = 1n // This holds the position value of base 10 digits
        
//         while (currentNode !== null) {
//             num = num + digitValue * BigInt(currentNode.val);
            
//             digitValue = digitValue * 10n ;
//             currentNode = currentNode.next;
//         }
        
//         return num
//     }

    
//     let num2ll = function(num) {
//         head = {
//             val:0,
//             next:null
//         }
//         let currentNode = head;
//         let digit = Number(num % 10n);
//         currentNode.val = digit;
//         num = num/10n
        
//         let newNode = null
//         while (num > 0) {
//             digit = Number(num % 10n);
//             newNode = {
//                 val:digit,
//                 next:null
//             }
//             currentNode.next = newNode;
//             currentNode = newNode;
//             num = num/10n
//         }
            
//         return head
//     }
        
//     let num1 = ll2num(l1);
//     let num2 = ll2num(l2);
    
//     console.log("num1=",num1);
//     console.log("num2=",num2);
    
//     let numRet = num1+num2;
            
//     return num2ll(numRet)

    /***************************************************************/
    /*    End version 1 code                                     */
    /***************************************************************/
    
    
    /***************************************************************/
    /*    Begin version 2 code                                     */
    /***************************************************************/
    head = {
        val:0,
        next:null
    }
    let currNodeOut = head;
    let currNodeL1 = l1;
    let currNodeL2 = l2;
    let digitL1 = null;
    let digitL2 = null;
    let digitOut = null;
    let carry = 0;
    let newNodeOut = null;
    
    
    if (currNodeL1 !== null) {
        digitL1 = currNodeL1.val;
        currNodeL1 = currNodeL1.next;
    }
    else {
        digitL1 = 0;
    }
    
    if (currNodeL2 !== null) {
        digitL2 = currNodeL2.val;
        currNodeL2 = currNodeL2.next;
    }
    else {
        digitL2 = 0;
    }
    
    digitOut = (digitL1+digitL2) % 10;
    carry = Math.floor((digitL1+digitL2)/10);
    
    currNodeOut.val = digitOut;
    
    while((currNodeL1 !== null) || (currNodeL2 !== null) || (carry >0)) {
        newNodeOut = {
            val:0,
            next:null
        }
        currNodeOut.next = newNodeOut;
        currNodeOut = newNodeOut;
        
        if (currNodeL1 !== null) {
            digitL1 = currNodeL1.val;
            currNodeL1 = currNodeL1.next;
        }
        else {
            digitL1 = 0;
        }
    
        if (currNodeL2 !== null) {
            digitL2 = currNodeL2.val;
            currNodeL2 = currNodeL2.next;
        }
        else {
            digitL2 = 0;
        }

        digitOut = (digitL1+digitL2+carry) % 10;
        carry = Math.floor((digitL1+digitL2+carry)/10);

        currNodeOut.val = digitOut;
        
        
        
        
    }
    
    return head;
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    /***************************************************************/
    /*    End version 2 code                                     */
    /***************************************************************/
    
    
    
    
    
    
    
    
    
    
    
};
