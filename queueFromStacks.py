class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.aux = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # transfer everything from queue to aux stack
        while not self.empty():
            item = self.queue.pop()
            self.aux.append(item)

        # add item to front of queue
        self.queue.append(x)

        # transfer everything from aux stack back to queue, on top of the item we just inserted
        while len(self.aux):
            item = self.aux.pop()
            self.queue.append(item)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.empty():
            return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)

for i in range(4):
    print("peek", obj.peek())
    print("pop", obj.pop(), "\n")


