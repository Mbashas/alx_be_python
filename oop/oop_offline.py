# # class Person:
# #     count = 0  # Class variable to count instances

# #     def __init__(self, name):
# #         self.name = name
# #         Person.count += 1  # Increment count on instance creation

# #     @classmethod
# #     def display_count(cls):
# #         print(f"Total persons created: {cls.count}")

# # # Usage
# # person1 = Person("Alice")
# # person2 = Person("Bob")
# # Person.display_count()  # Output: Total persons created: 2

# class Animal:
#   def make_sound(self):
#     print("Generic animal sound")

# class Dog(Animal):
#   def make_sound(self):
#     print("Woof!")

# animals = [Dog(), Animal()]
# for animal in animals:
#   animal.make_sound()
"""
def greet(name):
    return f"Hello, {name}!"


def execute_function(func, arg):
    return func(arg)

def square(x):
    return x * x

print(execute_function(square, 5)) # Output: 25
print(execute_function(greet, "Bob")) # Output: Hello, Bob!

def create_greeter(language):
    if language == "en":
        def english_greet(name):
            return f"Hello, {name}!"
        return english_greet
    elif language == "es":
        def spanish_greet(name):
            return f"¡Hola, {name}!"
        return spanish_greet

greet_in_english = create_greeter("es")
print(greet_in_english("Charlie")) # Output: Hello, Charlie!"""

import random

class TrapArtist:
    def __init__(self, name):
        self.name = name

    # This method doesn't need 'self' to work, but Python forces it!
    def pick_random_genre_BAD(self):
        genres = ["Trap", "Drill", "Mumble Rap"]
        return random.choice(genres)

artist = TrapArtist("Cardi B")
print(artist.pick_random_genre_BAD()) # Still needs an instance to call it