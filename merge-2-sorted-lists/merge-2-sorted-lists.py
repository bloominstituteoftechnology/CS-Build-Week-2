# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize head to list node 0      
        head = ListNode(0)
        ptr = head
        
        while True:
            # check for nodes in both lists
            if l1 is None and l2 is None:
                # if both lists are empty, loop is done
                break
            # if the first list is empty but second is not
            elif l1 is None:
                # return all of the second list
                ptr.next = l2
                break
            # if the second list is empty but first is not
            elif l2 is None:
                # return all of first list
                ptr.next = l1
                break
            else:         
                # set temporary head of 0 
                smallerVal = 0
                # check if value of next node in l1 is less than in l2
                if l1.val < l2.val:
                    smallerVal = l1.val
                    # if that's the case, insert into new list and move pointer to next
                    l1 = l1.next
                else:
                    # if value in l2 is greater than in l1, insert into new list 
                    smallerVal = l2.val
                    # then move the pointer to the next node in l2
                    l2 = l2.next
                    
                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr = ptr.next
                
        return head.next