"""import function_part1

function_part1.check_number(91)"""

"""from functions import function_part1
from functions import data_structures

function_part1.check_number(9)

data_structures.great("Alex")

"""

import os  # Module for interacting with the operating system

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# Example 1: Global and Local Scope
global_var = "I am global"

def scope_example():
    local_var = "I am local"
    print("Inside function:", local_var)
    print("Global variable inside function:", global_var)

scope_example()
print("Global variable outside function:", global_var)
# print(local_var)  # This would raise an error because local_var is not accessible here

# Example 2: Enclosing Scope (Nested Functions)
def outer_function():
    outer_var = "I am in outer function"
    
    def inner_function():
        inner_var = "I am in inner function"
        print("Inner function:", inner_var)
        print("Outer variable in inner function:", outer_var)
    
    inner_function()
    print("Outer function:", outer_var)
    # print(inner_var)  # This would raise an error because inner_var is not accessible here

outer_function()

# Example 3: Module Namespace
import math
print("Pi from math module:", math.pi)

# Example 4: Built-in Namespace
print("Built-in function len:", len("Hello"))
print("Built-in function max:", max(1, 2, 3))

# Example 5: Nonlocal Keyword
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        print("Count:", count)
    
    increment()
    increment()

counter()

