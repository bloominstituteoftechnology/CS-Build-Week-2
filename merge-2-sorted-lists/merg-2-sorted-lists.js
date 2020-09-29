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
var mergeTwoLists = function(l1, l2) {
  function merge(left, right) {
      if(!left) return right;
      if(!right) return left;
      
      if(left.val < right.val) {
          left.next = merge(left.next, right);
          return left;
      }
      right.next = merge(left, right.next);
      return right;
  }
  return merge(l1, l2);
};