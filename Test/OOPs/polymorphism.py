class Animal:

    def sound(self):
        pass

class Dog:
    def sound(self):
        return "Woof!"
    
class Cat:
    def sound(self):
        return "Meow!"
    
def make_sound(animal):
    print(animal.sound())

cat=Cat()
dog=Dog()

make_sound(cat)
make_sound(dog)