limit=int(input("Enter a limit: "))

sum=0
for i in range(1,limit+1,2):
    sum+=i
print("Sum of odd numbers: "+str(sum))