"""
Parser module for the compiler.

This module is responsible for parsing the stream of tokens generated by the
lexer. The parser is implemented as a recursive descent parser.
"""
import ply.yacc as yacc

from x_lexer import tokens
from classes.stack import Stack
from classes.symbols import Symbol, SymbolTable
from classes.quadruples import QuadrupleList
from classes.semantic import validate_semantics
from classes.memory import MemoryAssigner
from classes.exceptions import (
    UndeclaredError,
    InvalidTypeError,
)

# Global variable to store the symbol table
function_directory = None
# Scope stack (function declaration)
scope_stack = Stack('scope_stack')
# ID stack (variable declaration)
id_stack = Stack('id_stack')
# Jump Stack (conditions and cycles)
jump_stack = Stack('jump_stack')
# Function Call Stack (function calls)
f_call_stack = Stack('f_call_stack')
# Function Call Param Stack (function calls)
f_call_param_stack = Stack('f_call_param_stack')
# Function Call Param Type Stack (function calls)
f_call_param_type_stack = Stack('f_call_param_type_stack')
# Operator Stack (expressions)
operator_stack = Stack('operator_stack')
# Operand Stack (expressions)
operand_stack = Stack('operand_stack')
# Operator Type Stack (expressions)
operand_type_stack = Stack('operand_type_stack')
# Quadruple List
quadruples = QuadrupleList()
# Memory Assigner
memory_assigner = MemoryAssigner()

def p_prog(p):
    """PROG : PROG_N1 PROG_N2 SEMICOLON PROG_1 PROG_N3 BODY END"""
    # print('Function Directory:', function_directory)
    # print('Global:', function_directory.lookup(scope_stack.pop()).child)
    # print('Quadruples:')
    # print(quadruples)
    # memory_assigner.display()

def p_prog_n1(p):
    """PROG_N1 : PROGRAM"""
    global function_directory
    function_directory = SymbolTable()
    quadruples.add('GOTO', -1, -1, -1)
    jump_stack.push(quadruples.current())

def p_prog_n2(p):
    """PROG_N2 : ID"""
    function_directory.declare(
        Symbol(
            name=p[1],
            type='table.global',
            child=SymbolTable()
        )
    )
    scope_stack.push(p[1])

def p_prog_1(p):
    """PROG_1 : VARS PROG_2 
            | empty
    """

def p_prog_2(p):
    """PROG_2 : FUNCS PROG_2
            | empty
    """

def p_vars(p):
    """VARS : VARS_N1 VARS_1"""

def p_prog_n3(p):
    """PROG_N3 : MAIN"""
    main = jump_stack.pop()
    quadruples.fill(main, quadruples.current() + 1)

def p_vars_n1(p):
    """VARS_N1 : VAR"""
    if not function_directory.lookup(scope_stack.peek()).child:
        scope_vars = function_directory.lookup(scope_stack.peek())
        scope_vars.child = SymbolTable()
        function_directory.update(scope_vars)

def p_vars_1(p):
    """VARS_1 : VARS_N2 VARS_2"""
    
def p_vars_n2(p):
    """VARS_N2 : ID"""
    id_stack.push(p[1])

def p_vars_2(p):
    """VARS_2 : TWO_DOTS VARS_N3 SEMICOLON VARS_3
            | COMMA VARS_1
    """

def p_vars_n3(p):
    """VARS_N3 : TYPE"""
    for id in id_stack.items():
        memory_address = memory_assigner.assign(f'g_{p[1]}')
        scope_vars = function_directory.lookup(scope_stack.peek())
        scope_vars.child.declare(
            Symbol(
                name=id,
                type=f'var.{p[1]}',
                address=memory_address
            )
        )
        function_directory.update(scope_vars)
    id_stack.clear()

def p_vars_3(p):
    """VARS_3 : VARS_1
            | empty
    """

def p_funcs(p):
    """FUNCS : VOID FUNCS_N1 BRACKET_OPEN FUNCS_1 BRACKET_CLOSE SQ_BRACKET_OPEN FUNCS_N4 BODY SQ_BRACKET_CLOSE FUNCS_N3"""

def p_funcs_n1(p):
    """FUNCS_N1 : ID"""
    memory_address = memory_assigner.assign('g_void')
    function_directory.declare(
        Symbol(
            name=p[1],
            type='table.local',
            child=SymbolTable(),
            address=memory_address
        )
    )
    scope_stack.push(p[1])

def p_funcs_1(p):
    """FUNCS_1 : FUNCS_2
            | empty
    """

def p_funcs_2(p):
    """FUNCS_2 : FUNCS_N2 FUNCS_3
            | empty
    """

def p_funcs_n2(p):
    """FUNCS_N2 : ID TWO_DOTS TYPE"""
    memory_address = memory_assigner.assign(f'l_{p[3]}')
    scope_vars = function_directory.lookup(scope_stack.peek())
    scope_vars.child.declare(Symbol(name=p[1], type=f'param.{p[3]}', address=memory_address))
    function_directory.update(scope_vars)

def p_funcs_n3(p):
    """FUNCS_N3 : SEMICOLON"""
    scope_stack.pop()
    quadruples.add('ENDFUNC', -1, -1, -1)
    # print(f'Functon: {scope_to_pop}', function_directory.lookup(scope_to_pop).child)

def p_funcs_3(p):
    """FUNCS_3 : COMMA FUNCS_2
            | empty
    """

def p_funcs_n4(p):
    """FUNCS_N4 : VARS
            | empty
    """
    scope_vars = function_directory.lookup(scope_stack.peek())
    scope_vars.update_index(quadruples.current() + 1)
    function_directory.update(scope_vars)

def p_type(p):
    """TYPE : INT
            | FLOAT
    """
    p[0] = p[1]

def p_body(p):
    """BODY : CURLY_BRACKET_OPEN BODY_1"""

def p_body_1(p):
    """BODY_1 : STATEMENT BODY_1
            | CURLY_BRACKET_CLOSE
    """

def p_statement(p):
    """STATEMENT : ASSIGNMENT
                | CONDITION
                | CYCLE
                | F_CALL
                | PRINTS
    """

def p_assignment(p):
    """ASSIGNMENT : ASSIGNMENT_N1 ASSIGNMENT_N2 ASSIGNMENT_N3 SEMICOLON"""

def p_assignment_n1(p):
    """ASSIGNMENT_N1 : IDENTIFIER"""

def p_assignment_n2(p):
    """ASSIGNMENT_N2 : ASSIGN"""
    operator_stack.push(p[1])

def p_assignment_n3(p):
    """ASSIGNMENT_N3 : EXPRESSION"""
    if operator_stack.peek() == '=':
        operator = operator_stack.pop()
        operand = operand_stack.pop()
        operand_type = operand_type_stack.pop()
        assignee = operand_stack.pop()
        assignee_type = operand_type_stack.pop()

        result = assignee
        result_type = validate_semantics(assignee_type, operand_type, operator)
        
        quadruples.add(operator, operand, -1, result)

        operand_stack.push(result)
        operand_type_stack.push(result_type)

def p_condition(p):
    """CONDITION : IF BRACKET_OPEN EXPRESSION CONDITION_N1 BODY CONDITION_1"""

def p_condition_n1(p):
    """CONDITION_N1 : BRACKET_CLOSE"""
    expression_type = operand_type_stack.pop()

    if expression_type != 'bool':
        raise InvalidTypeError('Condition expression must be of type bool')
    else:
        expression_result = operand_stack.pop()
        quadruples.add('GOTOF', expression_result, -1, -1)
        jump_stack.push(quadruples.current())

def p_condition_1(p):
    """CONDITION_1 : CONDITION_N3 BODY CONDITION_N2
                | SEMICOLON
    """

def p_condition_n2(p):
    """CONDITION_N2 : SEMICOLON"""
    end = jump_stack.pop()
    quadruples.fill(end, quadruples.current() + 1)

def p_condition_n3(p):
    """CONDITION_N3 : ELSE"""
    quadruples.add('GOTO', -1, -1, -1)
    false = jump_stack.pop()
    jump_stack.push(quadruples.current())
    quadruples.fill(false, quadruples.current() + 1)

def p_cycle(p):
    """CYCLE : CYCLE_N1 BODY WHILE BRACKET_OPEN EXPRESSION CYCLE_N2 SEMICOLON"""

def p_cylce_n1(p):
    """CYCLE_N1 : DO"""
    jump_stack.push(quadruples.current() + 1)

def p_cycle_n2(p):
    """CYCLE_N2 : BRACKET_CLOSE"""
    expression_type = operand_type_stack.pop()

    if expression_type != 'bool':
        raise InvalidTypeError('Cycle expression must be of type bool')
    else:
        expression_result = operand_stack.pop()
        quadruples.add('GOTOT', expression_result, -1, jump_stack.pop())

def p_f_call(p):
    """F_CALL : F_CALL_N1 F_CALL_N4 F_CALL_1"""

def p_f_call_n1(p):
    """F_CALL_N1 : ID"""
    function_directory.lookup(p[1])
    f_call_stack.push(p[1])

def p_f_call_1(p):
    """F_CALL_1 : F_CALL_N2 F_CALL_2"""

def p_f_call_n2(p):
    """F_CALL_N2 : EXPRESSION"""
    f_call_param_stack.push(operand_stack.pop())
    f_call_param_type_stack.push(operand_type_stack.pop())
    quadruples.add('PARAM', f_call_param_stack.peek(), -1, f_call_param_stack.size() - 1)

def p_f_call_2(p):
    """F_CALL_2 : COMMA F_CALL_1
                | BRACKET_CLOSE F_CALL_N3
    """

def p_f_call_n3(p):
    """F_CALL_N3 : SEMICOLON"""
    function_id = f_call_stack.pop()
    function_table = function_directory.lookup(function_id)
    function_params = [symbol[1] for symbol in function_table.child.symbols.items() if symbol[1].type.split('.')[0] == 'param']

    if len(function_params) != len(f_call_param_stack.items()):
        raise InvalidTypeError(f'Function {function_id} expects {len(function_params)} parameters, {len(f_call_param_stack.items())} given')
    
    recieved_param_types = f_call_param_type_stack.items()

    for i in range(len(function_params)):
        fp_type = function_params[i].type.split('.')[-1]
        rp_type = recieved_param_types[i].split('.')[-1]

        if fp_type != rp_type:
            raise InvalidTypeError(f'Function {function_id} expects parameter {i + 1} of type {fp_type}, {rp_type} given')        

    quadruples.add('GOSUB', function_table.address, -1, function_table.index)

    f_call_param_stack.clear()
    f_call_param_type_stack.clear()

def p_f_call_n4(p):
    """F_CALL_N4 : BRACKET_OPEN"""
    function_address = function_directory.lookup(f_call_stack.peek()).address
    quadruples.add('ERA', function_address, -1, -1)

def p_prints(p):
    """PRINTS : PRINT BRACKET_OPEN PRINTS_1"""

def p_prints_1(p):
    """PRINTS_1 : PRINTS_N1 PRINTS_2"""

def p_prints_n1(p):
    """PRINTS_N1 : EXPRESSION
                | CONSTANT_STRING
    """
    quadruples.add('PRINT', operand_stack.pop(), -1, -1)
    operand_type_stack.pop()

def p_prints_2(p):
    """PRINTS_2 : COMMA PRINTS_1
            | BRACKET_CLOSE SEMICOLON
    """

def p_expression(p):
    """EXPRESSION : EXP EXPRESSION_1"""

def p_expression_1(p):
    """EXPRESSION_1 : EXPRESSION_N1 EXPRESSION_N2
                    | empty
    """

def p_expression_n1(p):
    """EXPRESSION_N1 : LESS_THAN
                    | MORE_THAN
                    | LESS_THAN_EQUAL
                    | MORE_THAN_EQUAL
                    | EQUAL
                    | NOT_EQUAL
    """
    operator_stack.push(p[1])

def p_expression_n2(p):
    """EXPRESSION_N2 : EXP"""
    if operator_stack.peek() in ['<', '>', '<=', '>=', '==', '!=']:
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        right_operand_type = operand_type_stack.pop()
        left_operand = operand_stack.pop()
        left_operand_type = operand_type_stack.pop()

        result_type = validate_semantics(left_operand_type, right_operand_type, operator)
        result_address = memory_assigner.assign(f't_{result_type}')

        quadruples.add(operator, left_operand, right_operand, result_address)

        operand_stack.push(result_address)
        operand_type_stack.push(result_type)

def p_exp(p):
    """EXP : EXP_N1 EXP_1"""

def p_exp_n1(p):
    """EXP_N1 : TERM"""
    if operator_stack.peek() in ['+', '-']:
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        right_operand_type = operand_type_stack.pop()
        left_operand = operand_stack.pop()
        left_operand_type = operand_type_stack.pop()

        result_type = validate_semantics(left_operand_type, right_operand_type, operator)
        result_address = memory_assigner.assign(f't_{result_type}')

        quadruples.add(operator, left_operand, right_operand, result_address)

        operand_stack.push(result_address)
        operand_type_stack.push(result_type)

def p_exp_1(p):
    """EXP_1 : EXP_N2 EXP
            | empty
    """

def p_exp_n2(p):
    """EXP_N2 : ADD
            | SUBTRACT
    """
    operator_stack.push(p[1])

def p_term(p):
    """TERM : TERM_N1 TERM_1"""

def p_term_n1(p):
    """TERM_N1 : FACTOR"""
    if operator_stack.peek() in ['*', '/']:
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        right_operand_type = operand_type_stack.pop()
        left_operand = operand_stack.pop()
        left_operand_type = operand_type_stack.pop()

        result_type = validate_semantics(left_operand_type, right_operand_type, operator)
        result_address = memory_assigner.assign(f't_{result_type}')

        quadruples.add(operator, left_operand, right_operand, result_address)

        operand_stack.push(result_address)
        operand_type_stack.push(result_type)

def p_term_1(p):
    """TERM_1 : TERM_N2 TERM
            | empty
    """

def p_term_n2(p):
    """TERM_N2 : MULTIPLY
            | DIVIDE
    """
    operator_stack.push(p[1])

def p_factor(p):
    """FACTOR : FACTOR_N1 EXPRESSION FACTOR_N2
            | FACTOR_N3 FACTOR_1 FACTOR_N4
            | FACTOR_1
    """

def p_factor_n1(p):
    """FACTOR_N1 : BRACKET_OPEN"""
    operator_stack.push(p[1])

def p_factor_n2(p):
    """FACTOR_N2 : BRACKET_CLOSE"""
    operator_stack.pop()

def p_factor_n3(p):
    """FACTOR_N3 : ADD
                | SUBTRACT
    """
    operator_stack.push(p[1])

def p_factor_n4(p):
    """FACTOR_N4 : empty"""
    operator = '*'
    right_operand = operand_stack.pop()
    right_operand_type = operand_type_stack.pop()
    left_operand = -1 if operator_stack.pop() == '-' else 1
    left_operand_type = 'int'

    result_type = validate_semantics(left_operand_type, right_operand_type, operator)
    result_address = memory_assigner.assign(f't_{result_type}')

    quadruples.add(operator, left_operand, right_operand, result_address)

    operand_stack.push(result_address)
    operand_type_stack.push(result_type)

def p_factor_1(p):
    """FACTOR_1 : CONSTANT
                | IDENTIFIER
    """

def p_identifier(p):
    """IDENTIFIER : ID"""
    id_symbol = None

    scopes = scope_stack.items()
    scopes.reverse()

    for scope in scopes:
        if function_directory.lookup(scope).child.lookup(p[1]):
            id_symbol = function_directory.lookup(scope).child.lookup(p[1])
            break
    
    if not id_symbol:
        raise UndeclaredError(f'Symbol {p[1]} is not declared')

    operand_stack.push(id_symbol.address)
    operand_type_stack.push(id_symbol.type)

def p_constant(p):
    """CONSTANT : CONSTANT_INT
                | CONSTANT_FLOAT
    """

def p_constant_int(p):
    """CONSTANT_INT : INT_CONST"""
    operand_address = memory_assigner.assign('c_int', p[1])
    operand_stack.push(operand_address)
    operand_type_stack.push('int')

def p_constant_float(p):
    """CONSTANT_FLOAT : FLOAT_CONST"""
    operand_address = memory_assigner.assign('c_float', p[1])
    operand_stack.push(operand_address)
    operand_type_stack.push('float')


def p_constant_string(p):
    """CONSTANT_STRING : STRING_CONST"""
    operand_address = memory_assigner.assign('c_string', p[1])
    operand_stack.push(operand_address)
    operand_type_stack.push('string')

def p_empty(p):
    """empty :"""
    pass

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}, token {p.type}")

# Build the parser
parser = yacc.yacc(debug=True)

def parse(data):
    """
    Parse the input data.
    
    Parameters:
    - data (str): The data to parse.

    Returns:
    - str: The output of the parser.
    """
    
    parser.parse(data)
    return (memory_assigner.constant_table, quadruples.output())
    