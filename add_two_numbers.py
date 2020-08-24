# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.






# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next




def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  carry_over = 0
  node1 = l1
  node2 = l2
  
  no_next = False
  list_start = None
  previous = None
  
  while no_next == False:
    num = node1.val + node2.val
    num += carry_over
    carry_over = num // 10
    num %= 10
    
    if previous != None:
      previous.next = ListNode(num, None)
      previous = previous.next
        
    
    if list_start == None:
      list_start = ListNode(num, None)
      previous = list_start
      
    
    if node1.next == None and node2.next == None and carry_over == 0:
      no_next = True
        
        
    if node1.next != None:
      node1 = node1.next
    else:
      node1 = ListNode(0, None)
        
        
    if node2.next != None:
      node2 = node2.next
    else:
      node2 = ListNode(0, None)
          
  return list_start