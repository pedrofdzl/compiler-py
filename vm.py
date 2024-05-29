import sys

from classes.stack import Stack
from classes.quadruples import QuadrupleList
from classes.memory import MemoryManager

memory_manager = MemoryManager()
function_exit_stack = Stack('function_exit_stack')

def execute(quadruples):
    ip = 0

    while ip < len(quadruples):
        quadruple = quadruples[ip]
        
        left_operand = memory_manager.access(quadruple.left_operand) if quadruple.left_operand != -1 else None
        right_operand = memory_manager.access(quadruple.right_operand) if quadruple.right_operand != -1 else None

        result = None

        if quadruple.operator == 1: # -
            result = left_operand - right_operand
        elif quadruple.operator == 2: # +
            result = left_operand + right_operand
        elif quadruple.operator == 3: #. *
            result = left_operand * right_operand
        elif quadruple.operator == 4: # /
            result = left_operand / right_operand
        elif quadruple.operator == 5: # <
            result = left_operand < right_operand
        elif quadruple.operator == 6: # >
            result = left_operand > right_operand
        elif quadruple.operator == 7: # <=
            result = left_operand <= right_operand
        elif quadruple.operator == 8: # >=
            result = left_operand >= right_operand
        elif quadruple.operator == 9: # ==
            result = left_operand == right_operand
        elif quadruple.operator == 10: #. !=
            result = left_operand != right_operand
        elif quadruple.operator == 11: # =
            result = left_operand
        elif quadruple.operator == 12: # PRINT
            print(left_operand)
        elif quadruple.operator == 13: # GOTO
            ip = quadruple.result
            continue
        elif quadruple.operator == 14: # GOTOF
            if not left_operand:
                ip = quadruple.result
                continue
        elif quadruple.operator == 15: # GOTOT
            if left_operand:
                ip = quadruple.result
                continue
        elif quadruple.operator == 16: # GOSUB
            function_exit_stack.push(ip + 1)
            ip = quadruple.result
            continue
        elif quadruple.operator == 17: # ERA
            # Allocate temporal memory
            memory_manager.allocate_local()
            memory_descriptor = memory_manager.descriptor['local'][quadruple.result]
            for type, value in memory_descriptor.items():
                memory_manager.allocate(type, value)
        elif quadruple.operator == 18: # ENDFUNC
            # Deallocate temporal memory
            memory_manager.deallocate_local()
            ip = function_exit_stack.pop()
            continue
        elif quadruple.operator == 19: # PARAM
            memory_manager.param(quadruple.left_operand)
        if result is not None:
            memory_manager.assign(quadruple.result, result)

        ip += 1


if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(f'out/{filename}', 'r') as file:
        # Allocate memory segments
        line = file.readline().strip()

        while line != '𓅭' and line != '𓃻':
            type, size = line.split('𓃱')
            memory_manager.describe(type=type, size=int(size))
            line = file.readline().strip()

        while line != '𓃻':
            line = file.readline().strip()  
            function = line
            line = file.readline().strip()

            while line != '𓅭' and line != '𓃻':
                type, size = line.split('𓃱')
                memory_manager.describe(type=type, size=int(size), function=int(function))
                line = file.readline().strip()

        # Allocate global memory
        for key, value in memory_manager.descriptor['global'].items():
            memory_manager.allocate(key, value)

        # Apply constants
        line = file.readline().strip()

        while line != '𓃻':
            address, value = line.split('𓃱')
            memory_manager.assign(int(address), value)
            line = file.readline().strip()

        # Read quadruples
        quadruples = QuadrupleList()

        line = file.readline().strip()

        while line:
            operator, left_operand, right_operand, result = line.split(' ')
            quadruples.add(int(operator), int(left_operand), int(right_operand), int(result))
            line = file.readline().strip()

        execute(quadruples.quadruples)