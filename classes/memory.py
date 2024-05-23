"""
Memory management module.

This module contains data structures and class functions for managing memory,
which is used in the intermediate representation of compiled code. Memory
is a common intermediate representation in compilers, representing the
allocation of memory for variables and tables.
"""

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
            'g_void': OFFSETS['g_void'],
            'g_int': OFFSETS['g_int'],
            'g_float': OFFSETS['g_float'],
            'l_int': OFFSETS['l_int'],
            'l_float': OFFSETS['l_float'],
            't_int': OFFSETS['t_int'],
            't_float': OFFSETS['t_float'],
            't_bool': OFFSETS['t_bool'],
            'c_int': OFFSETS['c_int'],
            'c_float': OFFSETS['c_float'],
            'c_string': OFFSETS['c_string'],
        }

    def assign(self, type, value=None):
        """
        Assign memory to a variable or constant.
        """
        if value is not None:
            if value not in self.constant_table:
                self.constant_table[value] = self.counter_table[type]
        
        assigned_address = self.counter_table[type]
        self.counter_table[type] += 1

        return assigned_address
    
    def display(self):
        """
        Display the memory allocation.
        """
        print('Constant Table:')
        for key, value in self.constant_table.items():
            print(f'{key}: {value}')
        print('\nCounter Table:')
        for key, value in self.counter_table.items():
            print(f'{key}: {value}')