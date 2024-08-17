"""multiple inheritance occurs when a class inherits from more than one parent class."""

class Parent1:
    def method1(self):
        print("Method from Parent1")

class parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1,parent2):
    def method3(self):
        print("Method from Child")

child_obj=Child()

child_obj.method1()
child_obj.method2()
child_obj.method3()

""" 'child' class inherits from both 'parent1' and 'parent2'. 
As a result, intances of the 'child' class have access to methods defined in both parent classes.
this is demostrated by calling 'method1()' and 'method2()' from the 'child' object, 
as well as the 'method3()' defined directly in the 'child' class"""