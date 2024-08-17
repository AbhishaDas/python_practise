"""Inheritance"""
# class P_class:
#     def perform(self,a,b):
#         return a+b
    
# class C_class(P_class):
#     pass

# obj=C_class()
# res=obj.perform(4,6)
# print("Sum: ",res)

"""abstraction"""
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
        
#     def calculate_area(self):
#         return 3.14*self.radius**2
    
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
        
#     def calculate_area(self):
#         return self.width*self.height
    
# circle_obj=Circle(3)
# rectangle_obj=Rectangle(2,3)
# print("Area of circle:", circle_obj.calculate_area())
# print("Area of Rectangle:", rectangle_obj.calculate_area())

"""encapsulation"""
# class Person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
        
#     def get_name(self):
#         return self._name
    
#     def get_age(self):
#         return self._age
    
#     def set_age(self,age):
#         if age>0:
#             self._age=age
#         else:
#             print("Enter a positive integer")

# obj=Person("Abhi",22)
# print("Name:",obj.get_name())
# print("Age:",obj.get_age())
# obj.set_age(24)
# print("Updated age:",obj.get_age())

"""polymorphism"""
# class Operation:
#     def perform(self,a,b):
#         pass
    
# class Addition:
#     def perform(self,a,b):
#         return a+b
    
# class Subtraction:
#     def perform(self,a,b):
#         return a-b
    
# add_obj=Addition()
# print("Addition:",add_obj.perform(2,3))

"""multiple Inheritance"""
# class Addition:
#     def add(self,a,b):
#         return a+b
    
# class Subtract:
#     def subtract(self,a,b):
#         return a-b
    
# class Operation(Addition,Subtract):
#     pass

# obj=Operation()
# print("Addition:",obj.add(2,3))
# print("Subtract:",obj.subtract(8,4))

"""multilevel inheritance"""
# class Superclass:
#     def mtd1(self):
#         print("method1 from superclass")
        
# class Parentclass(Superclass):
#     def mtd2(self):
#         print("method2 from parentclass")
        
# class Childclass(Parentclass):
#     pass

# obj=Childclass()

# obj.mtd1()
# obj.mtd2()

"""method overloading"""

    

    
        
    
    
    

