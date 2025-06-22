
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.year=year
#         self.model=model
#         self.odometer_reading= 0 #default

#     def get_descriptive_name(self):
#         full_name = f"{self.year}.{self.make}.{self.model}"
#         return full_name
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#         # The mileage parameter in update_odometer is also just a method parameter, not an instance attribute. It's only used to update the existing odometer_reading attribute. It's temporary and only exists within the scope of that method call.
#             self.odometer_reading=mileage
#         else:
#             print("You can't rollback an odometer!")

#     def increment_odometer(self,miles):
#         self.odometer_reading +=miles 
#         # The miles parameter in increment_odometer is just a method parameter, not an instance attribute - it's only used within that method to update the existing odometer_reading attribute.


# my_car = Car("Toyota","Cmary", 2020)
# print(my_car.get_descriptive_name())

# my_car.read_odometer()
# my_car.update_odometer(100)
# my_car.read_odometer()

# my_car.increment_odometer(50)
# my_car.read_odometer()

# my_car.update_odometer(149)  # This will trigger the message if current reading is higher
# my_car.read_odometer()


# Exercise one
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_student_info(self):
#      print(f"Name: {self.name} Age: {self.age}")

# student1 =Student("Alicia",9)

# student1.get_student_info()

# Exercise two
class Product:

    def __init__(self,name,price,quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity 
    
    def get_total_value(self):
        total_value = self.price*self.quantity
        return total_value
# product1=Product("Bio",100,4)
# product2=Product("Mui",89,2)


products = [ Product("Bio",100,4),
            Product("Mui",89,2)
]

total_value = 0
#print(f"The toal value of products in stock is {product1.get_total_value()}")
for product in products:
    total_value += product.get_total_value()
    
# OR total_value = sum(product.get_total_value() for product in products)
print(f"The total value of products: {total_value}")

