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
        
        if node1 is None: 
            s.next = node2
            return
        if node2 is None: 
            s.next = node1
            return
            
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
        
        return 'first node', first_node, first_node.next, first_node.next.next, first_node.next.next.next, first_node.next.next.next.next, first_node.next.next.next.next.next, first_node.next.next.next.next.next.next
    


#1-2-4 -1-3-4

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


print(merge_sorted(l1, l2))