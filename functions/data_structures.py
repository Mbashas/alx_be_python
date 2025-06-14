'''
my_list = [10, 20, 30, 40, 50]

print(my_list[::-1])

my_list.append(60)

print(my_list)

my_list.remove(60)

print(my_list)
'''

"""student = {"name": "Alice", "age": 20}
grade = student.get("name", "Not assigned")  # Returns "Not assigned"
print(grade)

for subject in student.keys():
    print(subject)  # Prints: name, age

for info in student.values():
    print(info)  # Prints: Alice, 20

for a, b in student.items():
    print(f"{a}: {b}")  # Prints: name: Alice, age: 20
"""

"""
my_list = [10, 20, 30, 40, 50]

my_list[0]=20

print(my_list)

# Tuple Immutability Example
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable
print("Tuple:", my_tuple)

# Set Operations Example
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: combines all unique elements from both sets
union_set = set_a.union(set_b)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: finds common elements between sets
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)  # Output: {3, 4}

# Difference: elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference:", difference_set)  # Output: {1, 2}

"""
import random
random_number = random.randint(1, 10)

print(random_number)

# Generate a random set of numbers between 1 and 10, remove duplicates, and display unique numbers
import random

# Generate a list of random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

# Convert the list to a set to remove duplicates
unique_numbers = set(random_numbers)

print("Random numbers:", random_numbers)
print("Unique numbers:", unique_numbers)

# Alternative implementation using a for loop
random_numbers_alt = []
for i in range(10):
    random_numbers_alt.append(random.randint(1, 10))

# Convert the list to a set to remove duplicates
unique_numbers_alt = set(random_numbers_alt)

print("Random numbers (alternative):", random_numbers_alt)
print("Unique numbers (alternative):", unique_numbers_alt)

def great(name):
    print(f"Hello {name}, How are you today?")
