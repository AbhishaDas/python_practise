class Calculator:
    def addition(self,a,b):
        return a+b
    
    def substraction(self,a,b):
        return a-b
    
    def multiplication(self,a,b):
        return a*b
    
    def division(self,a,b):
        return a/b

calculator=Calculator()    
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice (1/2/3/4): "))

if choice in [1,2,3,4]:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))

    if choice==1:
        result=calculator.addition(num1,num2)
        print("Result: "+str(result))

    elif choice==2:
        result=calculator.substraction(num1,num2)
        print("Result: "+str(result))

    elif choice==3:
        result=calculator.multiplication(num1,num2)
        print("Result: "+str(result))

    elif choice==4:
        result=calculator.division(num1,num2)
        print("Result: "+str(result))

else:
        print("Invalid Choice")

    



  
