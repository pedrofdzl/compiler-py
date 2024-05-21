"""
Stack implementation using list

This is a simple implementation of a stack using a list. 
The stack is a data structure that follows the Last In First Out
(LIFO) principle. This means that the last element added to the
stack is the first one to be removed.
"""

class Stack:
    """
    Stack class implementation using list.

    Attributes:
    - name (str): The name of the stack.
    - stack (list): The list that represents the stack.
    """

    def __init__(self, name = 'Stack'):
        self.name = name
        self.stack = []

    def push(self, item):
        """
        Push an item onto the stack.

        Parameters:
        - item: The item to be pushed onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Pop an item from the stack.

        Returns:
        - The item popped from the stack or None if the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        """
        Peek at the top item of the stack.

        Returns:
        - The top item of the stack or None if the stack is empty.
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        - bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Get the size of the stack.

        Returns:
        - int: The size of the stack.
        """
        return len(self.stack)
    
    def items(self):
        """
        Get the items of the stack.

        Returns:
        - list: The items of the stack.
        """
        return list(self.stack)
    
    def clear(self):
        """
        Clear the stack.
        """
        self.stack.clear()

    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return str(self)