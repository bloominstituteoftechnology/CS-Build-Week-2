# Implement the following operations of a queue using stacks.

#     push(x) -- Push element x to the back of queue.
#     pop() -- Removes the element from in front of queue.
#     peek() -- Get the front element.
#     empty() -- Return whether the queue is empty.

# Example:

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false

# Notes:

#     You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
#     Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
#     You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).




class MyQueue:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.queue = []
      

  def push(self, x: int) -> None:
    """
    Push element x to the back of queue.
    """
    self.queue.append(x)
      

  def pop(self) -> int:
    """
    Removes the element from in front of queue and returns that element.
    """
    return self.queue.pop(0)
      

  def peek(self) -> int:
    """
    Get the front element.
    """
    return self.queue[0]
      

  def empty(self) -> bool:
    """
    Returns whether the queue is empty.
    """
    if len(self.queue)>0:
      return False
    else:
      return True





