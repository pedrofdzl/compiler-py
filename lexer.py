"""
Lexical analysis module for the compiler.

This module contains the lexer for the compiler. The lexer is responsible for
converting the input source code into a stream of tokens. The lexer is
implemented as a generator that yields tokens one at a time.
"""

import ply.lex as lex

# Dict of reserved keywords
reserved_keywords = {
    'program': 'PROGRAM',
    'end': 'END',
    'main': 'MAIN',
    'var': 'VAR',
    'do': 'DO',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'int': 'INT',
    'float': 'FLOAT',
    'void': 'VOID',
}

# List of token names
tokens = [
    'ID',
    'INT_CONST',
    'FLOAT_CONST',
    'STRING_CONST',
    'LESS_THAN',
    'MORE_THAN',
    'LESS_THAN_EQUAL',
    'MORE_THAN_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
    'ASSIGN',
    'SQ_BRACKET_OPEN',
    'SQ_BRACKET_CLOSE',
    'BRACKET_OPEN',
    'BRACKET_CLOSE',
    'CURLY_BRACKET_OPEN',
    'CURLY_BRACKET_CLOSE',
    'MULTIPLY',
    'DIVIDE',
    'ADD',
    'SUBTRACT',
    'SEMICOLON',
    'TWO_DOTS',
    'COMMA',
] + list(reserved_keywords.values())

# Regular expression rules for simple tokens
t_LESS_THAN = r'<'
t_MORE_THAN = r'>'
t_LESS_THAN_EQUAL = r'<='
t_MORE_THAN_EQUAL = r'>='
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_ASSIGN = r'='
t_SQ_BRACKET_OPEN = r'\['
t_SQ_BRACKET_CLOSE = r'\]'
t_BRACKET_OPEN = r'\('
t_BRACKET_CLOSE = r'\)'
t_CURLY_BRACKET_OPEN = r'\{'
t_CURLY_BRACKET_CLOSE = r'\}'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_ADD = r'\+'
t_SUBTRACT = r'-'
t_SEMICOLON = r';'
t_TWO_DOTS = r':'
t_COMMA = r','
# Ignored characters
t_ignore = ' \t'

# Regular expression rules with some action code

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_keywords.get(t.value, 'ID')
    return t

def t_INT_CONST(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_FLOAT_CONST(t):
    r'[-+]?[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?'
    t.value = float(t.value)
    return t

def t_STRING_CONST(t):
    r'\"[^\"]*\"|\'[^\']*\''
    t.value = t.value[1:-1]
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'Illegal character {t.value[0]}')
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()