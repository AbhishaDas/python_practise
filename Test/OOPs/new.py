class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute
        self.__mileage = 0  # private attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def drive(self, miles):
        self.__mileage += miles


# Creating an instance of Car
my_car = Car("Toyota", "Camry", 2020)



# Accessing attributes using getter methods
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# Accessing and modifying attribute directly (not recommended due to encapsulation)
# This will throw an error because __make is a private attribute
# print("Make:", my_car.__make)

# Driving the car
my_car.drive(100)
print("Mileage:", my_car.get_mileage())  # Output: Mileage: 100
