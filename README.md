# Python Compiler Using PLY

This repository contains a Python compiler that leverages the PLY library. The compiler includes both a lexer and a parser module, responsible for lexical analysis and parsing, respectively.

## Introduction

The compiler is designed to process a custom programming language syntax, tokenize the input source code using the lexer, and construct an abstract syntax tree (AST) using the parser. It uses Python's PLY library, which is an implementation of lex and yacc parsing tools for Python.

## Installation

To run the compiler, you need Python installed on your machine along with the PLY library. You can install PLY using pip:

```bash
pip install ply
```

## About the Compiler

This compiler was created as part of a small senior year CS project and it is based around this diagram:

![Language Grammar Diagram](https://github.com/pedrofdzl/compiler-py/blob/ac4f42c0a7e8bb6fae1ccc99a7f4ec9250b9acba/Screenshot%202024-05-04%20at%202.41.19.png"Language Grammar Diagram")
