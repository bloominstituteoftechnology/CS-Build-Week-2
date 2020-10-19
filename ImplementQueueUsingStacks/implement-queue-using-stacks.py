
def foo():
    return

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_A = list()
        self.stack_B = list()

    def stack_A_push(self, val):
        """
        push value onto stack A
        """
        if val != None:
            self.stack_A.insert(0, val)

    def stack_A_pop(self):
        """
        pop and return value from stack A
        """
        if len(self.stack_A) == 0:
            return None

        ret_elm = self.stack_A[0]
        del self.stack_A[0]
        return ret_elm

    def stack_A_peek(self):
        """
        return value from stack A (but don't pop)
        """
        if len(self.stack_A) == 0:
            return None

        ret_elm = self.stack_A[0]
        return ret_elm

    def stack_B_push(self, val):
        """
        push value onto stack B
        """
        if val != None:
            self.stack_B.insert(0, val)

    def stack_B_pop(self):
        """
        pop and return value from stack A
        """
        if len(self.stack_B) == 0:
            return None

        ret_elm = self.stack_B[0]
        del self.stack_B[0]
        return ret_elm

    def stack_A2stack_B(self):
        """
        pops all stack A elements and
        pushes them onto stack B
        """
        tmp = self.stack_A_pop()
        while tmp != None:
            self.stack_B_push(tmp)
            tmp = self.stack_A_pop()

        return

    def stack_B2stack_A(self):
        """
        pops all stack B elements and
        pushes them onto stack A
        """
        tmp = self.stack_B_pop()
        while tmp != None:
            self.stack_A_push(tmp)
            tmp = self.stack_B_pop()

        return
        
    def push(self, x):
        """
        Push element x to the back of queue.
        """
        # Push all Stack A elements onto Stack B
        self.stack_A2stack_B()
        # Push x onto Stack A
        self.stack_A_push(x)
        # Push all Stack B elements onto Stack A
        self.stack_B2stack_A()

        return

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack_A_pop()    

    def peek(self):
        """
        Get the front element.
        """
        return self.stack_A_peek()
        
    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_A) == 0:
            return True

        return False
        

my_queue = MyQueue()
my_queue.push(1)
is_e = my_queue.empty()
my_queue.push(2)
is_e = my_queue.empty()
my_queue.pop()
is_e = my_queue.empty()
my_queue.pop()
is_e = my_queue.empty()

quit()

