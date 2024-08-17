class Bank:
    def __init__(self,acc_number,acc_balance):
        self.acc_number=acc_number
        self.acc_balance=acc_balance

    def deposit(self,amount):
        self.acc_balance=self.acc_balance+amount
        print(self.acc_balance)

    def withdrawal(self,amount):
        if self.acc_balance-amount>0:
            self.acc_balance=self.acc_balance-amount
            print(self.acc_balance) 
        
account1=Bank("A1432",1800)
account1.withdrawal(200)
account1.deposit(300)





    