"""
Quadruples module for compiler operations.

This module contains data structures and class functions for managing quadruples,
which are used in the intermediate representation of compiled code. Quadruples
are a common intermediate representation in compilers, representing operations
in a four-field structure: operator, left operand, right operand, and result.
"""

from classes.operators import OPERATORS_NUMERIC

class Quadruple:
    """
    This class represents a quadruple in the intermediate representation of compiled code.

    Attributes:
    - operator (str): The operator.
    - left_operand (str): The left operand.
    - right_operand (str): The right operand.
    - result (str): The result.
    """
    
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def __str__(self):
        return f'{self.operator} {self.left_operand} {self.right_operand} {self.result}'

    def __repr__(self):
        return str(self)


class QuadrupleBuilder:
    """
    Quadruple builder class for managing quadruples in the intermediate representation of compiled code.

    Attributes:
    - quadruples (list): The list of quadruples.
    """

    def __init__(self):
        self.quadruples = []
        
    def add(self, operator, left_operand, right_operand, result):
        """
        Add a new quadruple to the list.
        
        Parameters:
        - operator (str): The operator.
        - left_operand (str): The left operand.
        - right_operand (str): The right operand.
        - result (str): The result.
        """
        self.quadruples.append(Quadruple(OPERATORS_NUMERIC[operator], left_operand, right_operand, result))

    def current(self):
        """
        Get the current quadruple index.
        
        Returns:
        - int: The current quadruple index.
        """
        return len(self.quadruples) - 1
    
    def fill(self, index, value):
        """
        Fill a quadruple result.

        Parameters:
        - index (int): The quadruple index.
        - value (str): The value to fill.
        """
        self.quadruples[index].result = value

    def output(self):
        """
        Output the quadruples as text.

        Returns:
        - str: The quadruples as text format:
            operator left_operand right_operand result
            ...
        """
        return '\n'.join([f'{q.operator} {q.left_operand} {q.right_operand} {q.result}' for q in self.quadruples])

    def __str__(self):
        return '\n'.join([f'{str(i)} => ({str(q)})' for i, q in enumerate(self.quadruples)])
    
    def __repr__(self):
        return str(self)
    

class QuadrupleList:
    """
    Quadruple list class for managing quadruples in runtime.
    
    Attributes:
    - quadruples (list): The list of quadruples.
    """

    def __init__(self):
        self.quadruples = []

    def add(self, operator, left_operand, right_operand, result):
        """
        Add a new quadruple to the list.
        
        Parameters:
        - operator (str): The operator.
        - left_operand (str): The left operand.
        - right_operand (str): The right operand.
        - result (str): The result.
        """
        self.quadruples.append(Quadruple(operator, left_operand, right_operand, result))

    def get(self, index):
        """
        Get a quadruple by index.
        
        Parameters:
        - index (int): The index of the quadruple.
        
        Returns:
        - Quadruple: The quadruple at the index.
        """
        return self.quadruples[index]

    def __str__(self):
        return '\n'.join([str(q) for q in self.quadruples])
    
    def __repr__(self):
        return str(self)

    