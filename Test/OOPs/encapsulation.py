class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.__acc_no = acc_no #__used to represent the private variables
        self.__balance = balance

    def deposit(self, amount):
        if amount>0 :
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


myAcc = BankAccount("4321",800)

myAcc.deposit(200)
myAcc.withdraw(500)

print("Account Balance: "+str(myAcc.get_balance()))





        
