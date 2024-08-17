class Add:
    def sum(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    

obj=Add()
a=int(input("Enter 2 numbers: "))
b=int(input())
x=obj.sum(a,b)
print(x)