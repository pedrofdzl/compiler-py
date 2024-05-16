"""
Symbol tables for data structures module.
"""
from exceptions import (
    AlreadyDeclaredError,
    UndeclaredError,
    InvalidTypeError,
    InvalidOperationError,
)

class Symbol:
    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return f'{self.name}: {self.type}'

    def __repr__(self):
        return str(self)


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, symbol):
        if symbol.name in self.symbols:
            raise AlreadyDeclaredError(f'Symbol {symbol.name} is already declared.')
        self.symbols[symbol.name] = symbol

    def lookup(self, name):
        if name not in self.symbols:
            raise UndeclaredError(f'Symbol {name} is undeclared.')
        return self.symbols[name]
    
    def update(self, symbol):
        if symbol.name not in self.symbols:
            raise UndeclaredError(f'Symbol {symbol.name} is undeclared.')
        self.symbols[symbol.name] = symbol

    def remove(self, name):
        if name not in self.symbols:
            raise UndeclaredError(f'Symbol {name} is undeclared.')
        del self.symbols[name]

    def __str__(self):
        return '\n' + '\n'.join(str(symbol) for symbol in self.symbols.values())
