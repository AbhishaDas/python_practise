class Pclass:
    def sum(self,a,b):
        return a+b

class Cclass(Pclass):
    pass
    
obj= Cclass()
res=obj.sum(2,3)

print("Sum:",str(res))



