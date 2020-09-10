# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  # convert the linked lists to integers
  def conv_int(l: ListNode):
    s = ""
    while l != None:
      s += str(l.val)
      l = l.next
    return int(s[::-1])
    
  # convert sum of integers to a linked list
  def to_list(n: int):
    s = str(n)[::-1]
    head = prev = None
    for ch in s:
      node = ListNode(int(ch))
      if prev is not None:
        prev.next = node
        prev = node
      if head is None:
        head = prev
    return head
    
  # return the sum of the two linked lists
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = Solution.conv_int(l1)
    b = Solution.conv_int(l2)
    return Solution.to_list(a + b)
        