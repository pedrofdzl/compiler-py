"""
Semantic Cube for Compiler Operations module.

This module contains the semantic cube for the compiler operations.
"""

from exceptions import (
    InvalidOperationError,
)

semantic_cube = {
    'int': {
        'int': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'int',
            '*': 'int',
            '/': 'float',
            '+': 'int',
            '-': 'int',
        },
        'float': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'int',
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
        },
        'bool': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'int',
            '*': 'int',
            '/': 'int',
            '+': 'int',
            '-': 'int',
        }
    },
    'float': {
        'int': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'float',
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
        },
        'float': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'float',
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
        },
        'bool': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'float',
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
        }
    },
    'bool': {
        'int': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'error',
            '*': 'int',
            '/': 'int',
            '+': 'int',
            '-': 'int',
        },
        'float': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'error',
            '*': 'float',
            '/': 'float',
            '+': 'float',
            '-': 'float',
        },
        'bool': {
            '<': 'bool',
            '>': 'bool',
            '<=': 'bool',
            '>=': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'error',
            '*': 'int',
            '/': 'int',
            '+': 'int',
            '-': 'int',
        }
    }
}

def validate_semantics (left_operand_type, right_operand_type, operator):
    """
    Validate the types of the operands and the operator.

    This function validates the types of the operands and the operator
    using the semantic cube.

    Parameters:
    - left_operand_type (str): The type of the left operand.
    - right_operand_type (str): The type of the right operand.
    - operator (str): The operator.

    Returns:
    - str: The resulting type of the operation or an error if the operation is invalid.
    """
    try:
        left_operand_type = left_operand_type.split('.')[-1]
        right_operand_type = right_operand_type.split('.')[-1]
        
        result_type = semantic_cube[left_operand_type][right_operand_type][operator]
        if result_type == 'error':
            raise InvalidOperationError(f'Invalid operation: {left_operand_type} {operator} {right_operand_type}')
        return result_type
    except KeyError:
        raise InvalidOperationError(f'Invalid operation: {left_operand_type} {operator} {right_operand_type}')