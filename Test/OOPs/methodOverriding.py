class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Calculating area of circle")

class Square(Shape):
    def area(self):
        print("Calculating area of square")


circle = Circle()
circle.area()  

square = Square()
square.area()