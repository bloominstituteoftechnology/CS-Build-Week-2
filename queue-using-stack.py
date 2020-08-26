class MyQueue:
  
  def __init__(self):
    # Initialize myStack and tempStack with empty lists
    self.myStack, self.tempStack = [], []

  def push(self, x: int) -> None:
    # Append x elem to myStack
    self.myStack.append(x)

  def pop(self) -> int:
    # Pop oldest elem in queue by moving all myStack to tempStack putting oldest now at [0]
    if not self.tempStack:
      while self.myStack:
        self.tempStack.append(self.myStack.pop())
    top_elem = self.tempStack.pop()
    # Finally, put remaining elem back into myStack and get the top elem then return it
    while self.tempStack:
      self.myStack.append(self.tempStack.pop())
    return(top_elem)

    def empty(self) -> bool:

      return(not self.myStack)




    
