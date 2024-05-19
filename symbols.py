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
    def __init__(self, name, type, child=None):
        self.name = name # Name of the symbol
        self.type = type # Type of the symbol
        self.child = child # Symbol's child (when symbol is a table)

    def __str__(self):
        return f'{self.name}: {self.type}'

    def __repr__(self):
        return str(self)


class SymbolTable:
    def __init__(self):
        self.symbols = {} # Dictionary to store symbols (simulating table)

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
