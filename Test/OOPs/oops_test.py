"""inheritence"""

# class Parent_class:
#     def mul(self,a,b):
#         return a*b
    
# class Child_class(Parent_class):
#     pass

# obj=Child_class()

# result=obj.mul(6,8)

# print(result)

"""-------------------------------------------------------------------------------"""
"""abstraction"""
# from abc import ABC , abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area():
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def calculate_area(self):
#         return 3.14 * self.radius **2
    
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height

#     def calculate_area(self):
#         return self.width*self.height
    
# circle=Circle(4)
# rectangle=Rectangle(4,8)

# print("Area of circle: "+str(circle.calculate_area()))
# print("Area of rectanglr: "+str(rectangle.calculate_area()))

"""-----------------------------------------------------------------------------------"""

"""encapsulation"""

# class Person:
#     def __init__(self,name,age):
#         self._name =name
#         self._age =age

#     def get_name(self):
#         return self._name
    
#     def get_age(self):
#         return self._age
    
#     def set_age(self,age):
#         if age>0 :
#             self._age=age
            
#         else:
#             print("Enter a positive integer")

# obj=Person("Alice",20)

# print("Name:", obj.get_name())
# print("Age:",obj.get_age())

# obj.set_age(-2)

# obj.set_age(28)
# print("Updated age: ",obj.get_age())

"""----------------------------------------------------------------------"""

"""polymorphism"""
class Operation:
    def perform(self,a,b):
        pass

class Addition(Operation):
    def perform(self, a, b):
        return a+b
    
class Substraction(Operation):
    def perform(self, a, b):
        return a-b
    
class Multiplication(Operation):
    def perform(self, a, b):
        return a*b
    
addition=Addition()
substraction=Substraction()
multiplication=Multiplication()

print("Addition: ", addition.perform(9,5))
print("Substraction: ", substraction.perform(9,5))
print("Multiplication: ", multiplication.perform(9,5))

        




        
