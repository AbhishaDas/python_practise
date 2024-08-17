from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius **2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
circle = Circle(5)    
rectangle = Rectangle(2,4)

print("Area of Circle: " +str(circle.calculate_area()))
print(f"Area of Rectangle: {rectangle.calculate_area()}")

    




        

    