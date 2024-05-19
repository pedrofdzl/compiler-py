"""
Stack implementation using list

This is a simple implementation of a stack using a list. 
The stack is a data structure that follows the Last In First Out
(LIFO) principle. This means that the last element added to the
stack is the first one to be removed.
"""

class Stack:
    def __init__(self, name = 'Stack'):
        self.name = name
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    def items(self):
        return self.stack
    
    def clear(self):
        self.stack.clear()

    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return str(self)