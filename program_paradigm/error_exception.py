'''
number1= int(input("Input the fist number: "))
number2= int(input("Inpput the second number: "))
try:
    print(number1/number2)
except ZeroDivisionError:
    print("You can't divide by zero")
'''

'''
try:
    f = open('exploreoop.py')
except FileNotFoundError:
    print("File not found")
'''

# CUSTOM EXCEPTION

# class OutOfStockError(Exception):
#     """Custom exception for handling out-of-stock items."""

#     def __init__(self, item_name):
#         self.item_name = item_name

#     def __str__(self):
#         return f"Sorry, the item '{self.item_name}' is out of stock."

# # Sample Product Inventory
# product_inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 0,  # Out of stock
#     "grapes": 3
# }

# def purchase_item(item, quantity):
#     try:
#         if product_inventory[item] == 0:
#             raise OutOfStockError(item)
#         else:
#             print(f"Purchase successful: {quantity} {item}(s)")
#             product_inventory[item] -= quantity
  
#     except KeyError:
#         print(f"Sorry, '{item}' is not available in our inventory.")
# '''
#     if quantity <= 0:
#         raise ValueError("Quantity must be positive")
#     if quantity > product_inventory[item]:
#         raise OutOfStockError(f"Only {product_inventory[item]} {item}(s) available")
# '''
# # OPTION A: Handle all erros in functions
# '''
# def purchase_item(item, quantity):
#     if item not in product_inventory:
#         raise KeyError(f"Sorry, '{item}' is not available in our inventory.")
#     if product_inventory[item] == 0:
#         raise OutOfStockError(item)
#     # ... rest of the function
# '''

# # OPTION B :Let all erros propagate
# '''
# def purchase_item(item, quantity):
#     try:
#         if item not in product_inventory:
#             print(f"Sorry, '{item}' is not available in our inventory.")
#             return
#         if product_inventory[item] == 0:
#             print(f"Sorry, the item '{item}' is out of stock.")
#             return
#         # ... rest of the function
#     except Exception as e:
#         print(f"Error: {e}")
# '''
# # Testing the Custom Exception
# try:
#     purchase_item("apple", 3)  # Purchase successful
#     purchase_item("orange", 1)  # Raises OutOfStockError
#     purchase_item("watermelon", 1)  # Item not available
# except OutOfStockError as e:
#     print(e)  # Output:
# '''
# try:
#     purchase_item("apple", 3)  # Purchase successful
#     purchase_item("orange", 1)  # Raises OutOfStockError
#     purchase_item("watermelon", 1)  # Item not available
# except (OutOfStockError, KeyError) as e:
#     print(e)  # Output: Sorry, the item 'orange' is out of stock.
# '''

# # DOING IT MYSELF
# class OutOfStockError(Exception):
#     '''cUSTOM exception for handling out-of-stock items'''
#     def __init__(self, item_name):
#         self.item_name = item_name

#     def __str__(self):
#         return f"Sorry, the item '{self.item_name}' is out of stock."
    
# product_inventory = {"apple":0,"banana":2}

# def purchase_item(item,quantity):
#     try:
#         # By adding this "IF", we sort of block the execution of a sucess case when even the elment is not in the inventory and let except handle it. 
#         if product_inventory[item] == 0:
#             raise OutOfStockError(item)
#         else:
#             print(f"Purchase success:{quantity} {item}")
#             product_inventory[item] -= quantity
#     except KeyError:
#     #if it doesn't exit, it raises KeyError error, then have try and except     
#         print(f"Sorry, '{item}' is not available in our inventory.")
#     except OutOfStockError as e:
#         print(e)
#     #OR put another try-except during the instantiation 
   

# purchase_item("appley",2)
# purchase_item("apple",1)
# purchase_item("banana",1)

# Execise TWO (Firs implementation)
# class ValueTooHighError(Exception):
#     def __init__(self, number):
#         self.number = number
#     def __str__(self):
#         return f"Value {self.number} is greater than 100"
    
# number = int(input("Enter a number: "))

# try:
#     if number <= 100:
#         print(f"The number is {number}") 
#     else:
#         raise ValueTooHighError(number)
# except ValueTooHighError as e:
#     print(e)


# SECOND IMPLEMENTATION OR CHECK THE CHAT SATURDAY 14TH JUN

'''class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return f"Value {self.number} is greater than 100"
    
def check_number(number):
    if number > 100:
        raise ValueTooHighError(number)
    return number

try:
        # Get input from user
    number = float(input("Enter a number: "))
        
        # Check the number
    result = check_number(number)
    print(f"Valid number: {result}")
        
except ValueError:
    print("Error: Please enter a valid number.")
except ValueTooHighError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

'''

