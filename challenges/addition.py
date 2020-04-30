class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return f'{self.next}'

la = ListNode(2)
lb = ListNode(5)

la.next = ListNode(4)
la.next.next = ListNode(5)
la.next.next = ListNode(2)

lb.next = ListNode(6)
lb.next.next = ListNode(4)
lb.next.next = ListNode(4)

def addition(l1, l2): 
    sum = l1.val + l2.val
        #create a first node 
        #what if the sum is greater than 9? this step should be handled by the loop
    first_node = ListNode(sum)
        
        #current node is first_node, I want to make sure we can return the first node 
    current = first_node
        
        #loop will start with the second nodes 
    node1 = l1.next
    node2 = l2.next
            
        #while the both nodes are not none or while we have not reached the end of both lists
    while node1 or node2: 
        if current.next: 
            sum = current.next.val + node1.val + node2.val
        else: 
            sum = node1.val + node2.val
            
        if sum > 9: 
            if current.next: 
                current.next.val = sum % 10
                current.next.next = ListNode(sum / 10)
            else: 
                ones = ListNode(sum % 10)
                tens = ListNode(sum / 10)
                            
                ones.next = tens
                current.next = ones
        else: 
            if current.next: 
                current.next.val = sum
            else: 
                current.next = ListNode(sum)
        
        current = current.next 
        node1 = node1.next
        node2 = node2.next
                
        print('loop')       
            
                
        #return the first node we created        
    return first_node
            
print(addition(la, lb))