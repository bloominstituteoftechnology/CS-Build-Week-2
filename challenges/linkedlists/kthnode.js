class LinkedList {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
function removeKthNodeFromEnd(head, k) {
      let first = head;
      let second = head;
      let count = 0;
      
      //move first head k times ahead of second head
      for(i = 0; i < k; i++){
          first = first.next
      }
      
      if (first == null){
          head.value = head.next.value
          head.next = head.next.next
          return head
      }
      //iterate through the entire linked list until second reaches the last node
      while (first.next != null){
          second = second.next
          first = first.next 
      }
      
      
      second.next = second.next.next
      return head
  
  }

