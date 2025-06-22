'''
add = lambda x, y: x + y
result = add(5, 3)  
print(result)  # Output: 8

substract = lambda x,y,z: x/y + (z)

result = substract(4,2,3)

'''
''''
def user_info(name, age=None):
    """Prints user information."""
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")
user_info("Bob", 30)

'''



'''
# Function definition with default value
def greet(name="World"):
     """Prints a greeting message."""
     print(f"Hello, {name}!")
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice! 
'''


''''
def square(number):
 """Returns the square of a number."""
 return number * number
squared_value = square(4)  # squared_value will be 16
print(squared_value)
'''

'''
count = 0  # Global variable
def increment():
    global count
    count += 3  # This now refers to the global count
#increment()
print(count)  # Output: 0 (Global count remains unchanged)

'''
"""
def outer_function():
    count = 0  # Variable in enclosing scope
    
    def inner_function():
        nonlocal count  # Declares we want to modify the enclosing 'count'
        count += 1      # Now this modifies the outer count, not creates a new local one
        print(f"Count: {count}")
    
    inner_function()  # Output: Count: 1
    inner_function()  # Output: Count: 2
    print(f"Final count: {count}")  # Output: Final count: 2

outer_function()
"""

""""
def outer_function():
    x = 2  # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
outer_function()
"""

"""def great(name):
    print(f"Hello {name}, How are you today?")
great("Alliance")
"""
"""def calculate_area(width,height):
    area = width*height
    print("The area is",area)

calculate_area(12,32)"""

def check_number(number):
    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

check_number(5)