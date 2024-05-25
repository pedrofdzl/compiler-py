"""
Memory management module.

This module contains data structures and class functions for managing memory,
which is used in the intermediate representation of compiled code. Memory
is a common intermediate representation in compilers, representing the
allocation of memory for variables and tables.
"""

from classes.stack import Stack

OFFSETS = {
    'g_void': 500,
    'g_int': 1000,
    'g_float': 2000,
    't_int': 3000,
    't_float': 4000,
    't_bool': 5000,
    'c_int': 6000,
    'c_float': 7000,
    'c_string': 8000,
    'l_int': 9000,
    'l_float': 10000,
}

class MemoryAssigner:
    """
    This class manages the memory allocation for variables, parameters and constants in the
    compilation process.
    """

    def __init__(self):
        self.constant_table = {}
        self.counter_table = {
            'global': {
                'g_void': OFFSETS['g_void'],
                'g_int': OFFSETS['g_int'],
                'g_float': OFFSETS['g_float'],
                't_int': OFFSETS['t_int'],
                't_float': OFFSETS['t_float'],
                't_bool': OFFSETS['t_bool'],
                'c_int': OFFSETS['c_int'],
                'c_float': OFFSETS['c_float'],
                'c_string': OFFSETS['c_string'],
            },
            'local': {}
        }

    def assign(self, type, value=None):
        """
        Assign memory to a variable or constant.

        Parameters:
        - type (str): The type of memory to assign.
        - value: The value to assign (if any).
        """
        if value is not None:
            if value not in self.constant_table.keys():
                self.constant_table[value] = self.counter_table['global'][type]
            else:
                return self.constant_table[value]
        
        assigned_address = self.counter_table['global'][type]
        self.counter_table['global'][type] += 1

        return assigned_address
    
    def assign_local(self, function, type):
        """
        Assign memory to a local variable or constant.

        Parameters:
        - function (str): The name of the function.
        - type (str): The type of memory to assign.
        """
        if function not in self.counter_table['local']:
            self.counter_table['local'][function] = {
                'l_int': OFFSETS['l_int'],
                'l_float': OFFSETS['l_float'],
            }
        
        assigned_address = self.counter_table['local'][function][type]
        self.counter_table['local'][function][type] += 1

        return assigned_address
    
    def output(self):
        """
        Output the memory allocation.
        """
        counter_table_copy = self.counter_table

        for key, _ in counter_table_copy['global'].items():
            counter_table_copy['global'][key] -= OFFSETS[key]

        for key, value in counter_table_copy['local'].items():
            for key2, _ in value.items():
                counter_table_copy['local'][key][key2] -= OFFSETS[key2]

        return self.constant_table, counter_table_copy
    
    def display(self):
        """
        Display the memory allocation.
        """
        constant_table, counter_table = self.output()

        print('Constant Table:')
        for value, address in constant_table.items():
            print(f'{address}: {value}')

        print('\nGlobal Counter Table:')
        for key, value in counter_table['global'].items():
            print(f'{key}: {value}')

        print('\nLocal Counter Table:')
        for key, value in counter_table['local'].items():
            print(f'{key}:')
            for key2, value2 in value.items():
                print(f'  {key2}: {value2}')


class MemorySegment:
    """
    This class represents a dynamic memory segment in runtime.
    
    Attributes:
    - memory (list): The memory segment.
    - type (str): The type of memory segment [g_void, g_int, g_float, l_int, l_float, t_int, t_float, t_bool, c_int, c_float, c_string].
    """

    def __init__(self, type, size=0):
        if type not in OFFSETS.keys():
            raise ValueError(f'Invalid memory segment type: {type}')

        self.memory = [None] * size
        self.type = type

    def access(self, address):
        """
        Access a memory address.
        
        Parameters:
        - address (int): The memory address.
        
        Returns:
        - The value at the memory address.
        """
        index = address - OFFSETS[self.type]
        return self.memory[index] if index < len(self.memory) else None
    
    def assign(self, address, value):
        """
        Assign a value to a memory address.
        
        Parameters:
        - address (int): The memory address.
        - value: The value to assign.
        """
        index = address - OFFSETS[self.type]
        self.memory[index] = value
    
    def __str__(self):
        return f'{self.memory}'
    
    def __repr__(self):
        return str(self)
    

class MemoryManager:
    """
    This class manages the memory allocation for variables, parameters and constants in the
    runtime process.
    """

    def __init__(self):
        self.descriptor = {
            'global': {
                'g_void': 0,
                'g_int': 0,
                'g_float': 0,
                't_int': 0,
                't_float': 0,
                't_bool': 0,
                'c_int': 0,
                'c_float': 0,
                'c_string': 0,
            },
            'local': {}
        }
        self.memory = Stack('memory')

    def allocate(self, type, size=0):
        """
        Allocate memory for a memory segment.

        Parameters:
        - type (str): The type of memory segment [g_void, g_int, g_float, l_int, l_float, t_int, t_float, t_bool, c_int, c_float, c_string].
        - size (int): The size of the memory segment.
        """
        if not type.startswith('l'):
            if self.memory.size() == 0:
                self.memory.push({})
            self.memory.items()[0][type] = MemorySegment(type, size)
        else:
            self.memory.items()[-1][type] = MemorySegment(type, size)

    def allocate_local(self):
        """
        Allocate memory for a local memory segments.
        """
        self.memory.push({})

    def deallocate_local(self):
        """
        Deallocate memory for a memory segments.
        """
        self.memory.pop()

    def describe(self, type, size=0, function=None):
        """
        Describe a memory segment.
        """
        if function is not None:
            if function not in self.descriptor['local']:
                self.descriptor['local'][function] = {}
            self.descriptor['local'][function][type] = size
        else:
            self.descriptor['global'][type] = size

    def access(self, address):
        """
        Access a memory address.

        Parameters:
        - address (int): The memory address.
        """
        type = self._get_type(address)

        if type.startswith('l'):
            value = self.memory.peek()[type].access(address) if self.memory.peek()[type].access(address) is not None else self.memory.peek(2)[type].access(address)
        else:
            value = self.memory.first()[type].access(address)

        if type.endswith('void'):
            return None
        if type.endswith('int'):
            return int(value)
        if type.endswith('float'):
            return float(value)
        if type.endswith('bool'):
            return bool(value)
        if type.endswith('string'):
            return str(value)
        
        return value
    
    def assign(self, address, value):
        """
        Assign a value to a memory address.

        Parameters:
        - address (int): The memory address.
        - value: The value to assign.
        """
        type = self._get_type(address)

        if type.startswith('l'):
            memory_to_access = self.memory.items()[-1]
        else:
            memory_to_access = self.memory.items()[0]

        if type.endswith('int'):
            value = int(value)
        if type.endswith('float'):
            value = float(value)
        if type.endswith('bool'):
            value = bool(value)
        if type.endswith('string'):
            value = str(value)

        memory_to_access[type].assign(address, value)

    def param(self, address):
        """
        Copy a address value to a local memory segment.
        
        Parameters:
        - address (int): The memory address.
        """
        type = self._get_type(address)
        
        if type.startswith('l'):
            access_memory = self.memory.items()[-2]
        else:
            access_memory = self.memory.items()[0]

        value = access_memory[type].access(address)

        index = 0
        target_memory = self.memory.peek()

        if type.endswith('int'):
            target_type = 'l_int'
        if type.endswith('float'):
            target_type = 'l_float'
        
        while target_memory[target_type].access(OFFSETS[target_type] + index) is not None:
            index += 1

        target_memory[target_type].assign(OFFSETS[target_type] + index, value)

    def _get_type(self, address):
        """
        Get string type from memory address.
        """
        if address < OFFSETS['g_int']:
            return 'g_void'
        elif address < OFFSETS['g_float']:
            return 'g_int'
        elif address < OFFSETS['t_int']:
            return 'g_float'
        elif address < OFFSETS['t_float']:
            return 't_int'
        elif address < OFFSETS['t_bool']:
            return 't_float'
        elif address < OFFSETS['c_int']:
            return 't_bool'
        elif address < OFFSETS['c_float']:
            return 'c_int'
        elif address < OFFSETS['c_string']:
            return 'c_float'
        elif address < OFFSETS['l_int']:
            return 'c_string'
        elif address < OFFSETS['l_float']:
            return 'l_int'
        else:
            return 'l_float'
        
    def __str__(self):
        return str(self.memory)