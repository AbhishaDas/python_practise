class Area:
    def circle(self, radius):
        return 3.14 * radius ** 2

    def square(self, length):
        return length ** 2

    def rectangle(self, length, breadth):
        return length * breadth

    def triangle(self, base, height):
        return 0.5 * base * height


class MyClass(Area):
    def main(self):
        while True:
            print("\nEnter your choice:")
            print("1. Circle")
            print("2. Square")
            print("3. Rectangle")
            print("4. Triangle")
            print("5. Exit")
            choice = int(input())

            if choice == 1:
                radius = float(input("Enter the radius: "))
                area = self.circle(radius)
                print("Area of the circle is:", round(area, 2))
            elif choice == 2:
                length = float(input("Enter the length: "))
                area = self.square(length)
                print("Area of the square is:", round(area, 2))
            elif choice == 3:
                length = float(input("Enter the length: "))
                breadth = float(input("Enter the breadth: "))
                area = self.rectangle(length, breadth)
                print("Area of the rectangle is:", round(area, 2))
            elif choice == 4:
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                area = self.triangle(base, height)
                print("Area of the triangle is:", round(area, 2))
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
my_class_instance = MyClass()
my_class_instance.main()