# Python Compiler Using PLY

This repository contains a custom compiler implemented in Python that leverages the PLY library. The compiler includes both a lexer and a parser module, responsible for lexical analysis and parsing, respectively. The repository also contains a virtual machine that simulates memory management and a virtual machine to execute the compiled code.

## Table of Contents

- [Introduction](#introduction)
- [About the Compiler](#about-the-compiler)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Components](#components)
    - [Lexer](#lexer)
    - [Parser](#parser)
    - [Intermediate Representation](#intermediate-representation)
    - [Memory Management](#memory-management)
    - [Virtual Machine](#virtual-machine)
- [Contributing](#contributing)

## Introduction

The compiler is designed to process a custom programming language syntax, tokenize the input source code using the lexer, and construct an abstract syntax tree (AST) using the parser. It uses Python's PLY library, which is an implementation of lex and yacc parsing tools for Python.

## About the Compiler

This compiler was created as part of a small senior year CS project and it is based around this diagram:

![Language Grammar Diagram](https://github.com/pedrofdzl/compiler-py/blob/ac4f42c0a7e8bb6fae1ccc99a7f4ec9250b9acba/Screenshot%202024-05-04%20at%202.41.19.png)

## Installation

1. Clone the repository:

```bash
git clone git@github.com:pedrofdzl/compiler-py.git
```

2. Navitage to the project directory:

```bash
cd compiler-py
```

3. Create Python environment. It's recommended to use a virtual environment:

```bash
pipenv shell
```

4. To run the compiler, you need Python installed on your machine along with the PLY library. You can install PLY using pip:

```bash
pip install ply
```

## Usage

1. Choose or create a test file in the `/test` directory. You can see the compiler's grammar diagram for examples.

2. Compile the source file:

```bash
python compiler.py test.duck
```

3. Execute the compiled code:

```bash
python vm.py test.dk
```

## Project Structure

```bash
custom-compiler/
│
├── classes/
│   ├── exceptions.py          # Custom exception classes
│   ├── memory.py              # Memory management classes
│   ├── operators.py           # Operator definitions
│   ├── quadruples.py          # Quadruple and QuadrupleList classes
│   ├── stack.py               # Stack class
│   ├── symbols.py             # Symbol and SymbolTable classes
│   └── semantic.py            # Semantic validation functions
│
├── tests/
│   ├── test_file1.txt         # Example source file 1
│   └── test_file2.txt         # Example source file 2
│
├── out/
│   └── test_file1.dk       # Compiled output files
│
├── compiler.py                # Main compiler script
├── compiler.py                # Parse testing script
├── vm.py                      # Virtual machine script
├── x_lexer.py                 # Lexer module
├── x_parser.py                # Parser module
└── README.md                  # This README file
```

## Components

1. Lexer

    The lexer is responsible for tokenizing the source code. It converts the input source code into a stream of tokens that can be processed by the parser.

2. Parser

    The parser takes the stream of tokens generated by the lexer and builds the intermediate representation. It uses a recursive descent parser to analyze the syntax and semantics of the source code.

3. Intermediate Representation

    The intermediate representation is based on quadruples, which are a common format in compilers. Each quadruple consists of an operator, two operands, and a result.

4. Memory Management

    Memory management is handled by the MemoryAssigner and MemoryManager classes. These classes allocate memory for variables, constants, and temporary values used during execution.

5. Virtual Machine

    The virtual machine executes the compiled code represented by quadruples. It simulates a CPU by processing each quadruple and performing the corresponding operations.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your changes.
