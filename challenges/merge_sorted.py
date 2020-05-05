class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self): 
        return f'{self.val}'

def merge_sorted(l1, l2): 
    node1 = l1
    node2 = l2
    s = None
    first_node = None
    running = True
        
    if node1.val < node2.val: 
        first_node = node1
        s = first_node
        node1 = node1.next
    if node1.val > node2.val: 
        first_node = node2
        s = first_node
        node2 = node2.next
    if node1.val == node2.val: 
        first_node = node1
        node1 = node1.next
        first_node.next = node2
        s = first_node.next
        node2 = node2.next

    
        
    while node1 or node2: 
        
        if node1.next == None: 
            s.next = node1
            s.next.next = node2
            break

        if node2 == None: 
           s.next = node2
           s.next.next = node1 
           break
            
        if node1.val < node2.val: 
            s.next = node1
            node1 = node1.next
            s = s.next 
        if node1.val > node2.val: 
            s.next = node2
            node2 = node2.next
            s = s.next 
        if node1.val == node2.val: 
            s.next = node1
            s.next.next = node2
            s = s.next.next
            node1 = node1.next
            node2 = node2.next 
        
    return first_node
    


#1-2-4 -1-3-4

l1 = ListNode(5)
# l1.next = ListNode(6)
# l1.next.next = ListNode(9)

l2 = ListNode(10)
# l2.next = ListNode(11)
# l2.next.next = ListNode(12)


print(merge_sorted(l1, l2))