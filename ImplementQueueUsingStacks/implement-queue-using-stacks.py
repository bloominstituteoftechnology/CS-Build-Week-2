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

    def stack_A_ret_last(self):
        """
        This functions essentially pops the next queue value
        by returning the last value in the stack
        """
        # Does Stack A only have on 1 element?
        if len(self.stack_A) == 1:
            # yes: return the last element now
            # Pop the first element in the stack (last element in the queue)
            return self.stack_A_pop()

        # Stack A has more than one element
        lst_elm = self.stack_A_pop()
        while True:
            # Push value to Stack B
            self.stack_B_push(lst_elm)
            # Pop the next value from Stack A
            lst_elm = self.stack_A_pop()
            # Is this the last element in the stack
            if len(self.stack_A) == 0:
                # yes: have last element; break without pushing to Stack B
                break

        # Done popping from Stack A
        # Push all the values back from Stack B to Stack A
        self.stack_B2stack_A()

        return lst_elm
    
    def stack_A_peek_last(self):
        """
        This functions essentially peeks the next queue value
        by returning the last value in the stack but keepin the 
        value in the strack
        """
        lst_elm = self.stack_A_pop()
        while lst_elm != None:
            # Push value to Stack B
            self.stack_B_push(lst_elm)

            # Is lst_elm the actual last element?
            if len(self.stack_A) <= 1:
                # yes: break out of the loop
                break
            
            # Pop the next value from Stack A
            lst_elm = self.stack_A_pop()

        # Done popping from Stack A
        # Push all the values back from Stack B to Stack A
        self.stack_B2stack_A()

        return lst_elm

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
        return self.stack_A_ret_last()    

    def peek(self):
        """
        Get the front element.
        """
        return self.stack_A_peek_last()
        

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_A) == 0:
            return True

        return False
        

my_queue = MyQueue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_pop = my_queue.pop()
quit()
my_queue.push(3)
my_queue.push(4)
my_queue.push(5)
my_pop = my_queue.pop()
my_pop = my_queue.pop()
my_pop = my_queue.pop()
my_pop = my_queue.pop()
quit()
