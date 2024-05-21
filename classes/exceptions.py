"""
Exceptions module.

This module contains custom exceptions for the compiler.
"""

class CompilerError(Exception):
    """Base class for compiler exceptions."""
    pass


class AlreadyDeclaredError(CompilerError):
    """Exception raised when a symbol is already declared."""
    pass


class UndeclaredError(CompilerError):
    """Exception raised when a symbol is undeclared."""
    pass


class InvalidTypeError(CompilerError):
    """Exception raised when a symbol is of an invalid type."""
    pass


class InvalidOperationError(CompilerError):
    """Exception raised when an operation is invalid."""
    pass
