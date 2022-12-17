# Write here the code challenge solution

class MyQueue:
    """
    Class for implementing a queue using two stacks.
    """
    
    def __init__(self):
        """
        Initialize the enqueuing stack and dequeuing stack.
        """
        self.enqueuing_stack = []
        self.dequeuing_stack = []
    
    def push(self, x):
        """
        Push an element onto the enqueuing stack.
        """
        self.enqueuing_stack.append(x)
    
    def pop(self):
        """
        Pop the element at the front of the queue.
        """
        if not self.dequeuing_stack:
            # If the dequeuing stack is empty, move all elements from the enqueuing stack
            # onto the dequeuing stack.
            while self.enqueuing_stack:
                self.dequeuing_stack.append(self.enqueuing_stack.pop())
        return self.dequeuing_stack.pop()
    
    def peek(self):
        """
        Return the element at the front of the queue.
        """
        if not self.dequeuing_stack:
            # If the dequeuing stack is empty, move all elements from the enqueuing stack
            # onto the dequeuing stack.
            while self.enqueuing_stack:
                self.dequeuing_stack.append(self.enqueuing_stack.pop())
        return self.dequeuing_stack[-1]
    
    def empty(self):
        """
        Return True if the queue is empty, False otherwise.
        """
        return not self.enqueuing_stack and not self.dequeuing_stack
