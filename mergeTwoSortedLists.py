"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeList = []
        
        # check for input edge cases
        if getattr(l1, "val", None) == None:
            return l2
        elif getattr(l2, "val", None) == None:
            return l1
        
        # iterate l1 and l2, adding to list
        self.iterateList(l1, nodeList)
        self.iterateList(l2, nodeList)
        
        # sort list by node value
        nodeList.sort(key=lambda node:node.val)
        
        print(nodeList)
        
        # iterate list and set up .next for each node
        for idx,node in enumerate(nodeList):
            # edge case - final node
            if idx == len(nodeList)-1:
                node.next = None
            else:
                node.next = nodeList[idx+1]
                
        return nodeList[0]
        
    def iterateList(self, l: ListNode, nodeList: List) -> None:
        cur = l
        nodeList.append(cur)
        
        while cur.next:
            cur = cur.next
            nodeList.append(cur)
            
