"""
Quadruples module for compiler operations.

This module contains data structures and class functions for managing quadruples.
"""

class Quadruple:
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def __str__(self):
        return f'{self.operator} {self.left_operand} {self.right_operand} {self.result}'

    def __repr__(self):
        return str(self)


class QuadrupleList:
    def __init__(self):
        self.quadruples = []
        
    def add(self, operator, left_operand, right_operand, result):
        self.quadruples.append(Quadruple(operator, left_operand, right_operand, result))

    def current(self):
        return len(self.quadruples) - 1
    
    def fill(self, index, value):
        self.quadruples[index].result = value

    def __str__(self):
        return '\n'.join([f'{str(i)} => ({str(q)})' for i, q in enumerate(self.quadruples)])
    
    def __repr__(self):
        return str(self)


class TempManager:
    def __init__(self):
        self.temp_count = 0

    def new_temp(self):
        temp = f't{self.temp_count}'
        self.temp_count += 1
        return temp

    def reset(self):
        self.temp_count = 0

    def __str__(self):
        return f't{self.temp_count}'
    