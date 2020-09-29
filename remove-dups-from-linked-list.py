#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # curr = head
        # prev = None

        # # empty set b/c sets can't contain dups
        # s = set()

        # # do till linked list is not empty
        # while curr:
        #     # if curr node is seen before, ignore it
        #     if curr.val in s:
        #         prev.next = curr.next

        #     # insert curr node into the set and move to next node
        #     else:
        #         s.add(curr.val)
        #         prev = curr
            
        #     curr = prev.next
        # return head





        node = head
        while node:
            lead = node
            while node.next  and node.next.val == lead.val:
                node = node.next
            node = lead.next = node.next
        return head
    

    



        
# @lc code=end

