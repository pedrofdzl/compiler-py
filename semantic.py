"""
Semantic Cube for Compiler Operations module.

This module contains the semantic cube for the compiler operations.
"""

semantic_cube = {
    'int': {
        'int': {
            '<': 'bool',
            '>': 'bool',
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