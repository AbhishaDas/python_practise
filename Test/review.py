"""inheritance"""
# class Parent:
#     def operation(self,a,b):
#         return a+b
    
# class Child(Parent):
#     pass

# obj=Child()
# res=obj.operation(2,3)
# print(res)

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
#         self._age=age

# obj=Person("Alice",20)
# print("Name:",obj.get_name())
# print("Age",obj.get_age())

# obj.set_age(28)
# print("Updated Age:",obj.get_age())

"""abstraction"""

from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle:

    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14*self.radius**2
    
class Rectangle:

    def __init__(self,width,height):
        self.width
        self.height

    def calculate_area(self):
        return self.width*self.height

circle=Circle(6)
rect=Rectangle(8,2)

print("Area of circle: ",circle.calculate_area())

    




"""polymorphism"""

class operation:

    def perform(self,a,b):
        pass

class Addition(operation):
    def perform(self,a,b):
        return a+b
    
class Substract(operation):
    def perform(self,a,b):
        return a-b
    
add=Addition()
sub=Substract()

print(add.perform(2,3))
print(sub.perform(2,3))



    

    
