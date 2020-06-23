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

var addTwoNumbers = function (l1, l2) {
  // reverse the two linked lists
  const num1 = reverseLinkedList(l1);
  const num2 = reverseLinkedList(l2);

  // sum the numbers & reverse order
  const sum = computeReverseSum(num1, num2);

  // fill result array w/ linked list nodes
  let result = [];
  sum.forEach((digit) => {
    result.push(new ListNode(digit));
  });

  // link nodes
  result.forEach((node, index) => {
    node.next = result[index + 1];
  });

  // return LL head
  return result[0];
};

function reverseLinkedList(ll) {
  // create an empty "stack"
  const stack = [];
  // treat result as string for easier reversing
  let result = '';

  let cur = ll;
  stack.push(cur);
  // build up stack
  while (cur.next) {
    cur = cur.next;
    stack.push(cur);
  }

  // pop items off stack and add to result, reversing the order
  while (stack.length) {
    const node = stack.pop();
    result += node.val;
  }

  // cast result back to number and return
  return Number(result);
}

function computeReverseSum(num1, num2) {
  let sum = num1 + num2;
  // cast to string, reverse order of digits, then cast back to numbers
  let result = String(sum)
    .split('')
    .reverse()
    .map((char) => Number(char));

  return result;
}
