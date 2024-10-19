class Atm:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.balance = 0
    
    def Diposit(self,amount):
        self.balance+=amount
        print("Diposite Done = ",self.balance)
    
    def Withdrawal(self,amount1):
        if self.balance>=amount1:
            self.balance -= amount1
            print("Withdrawal Done =",amount1)
        else:
            print("Insufficient bal")

    def Check_balance(self):
        print("Total Balance =",self.balance)

obj = Atm(121,"Narendra")
obj.Diposit(1000)
obj.Check_balance()
obj.Withdrawal(200)
obj.Check_balance()

# class ATM:
#     def __init__(self):
#         self.amount = 0.0
        
#     def deposit(self, dep_amt):
#         self.amount = dep_amt
        
#     def withdraw(self, wd_amt):
#         if self.amount >= wd_amt:
#             self.amount -= wd_amt
#         else:
#             print("Insufficient bal")
    
#     def check_bal(self):
#         print(self.amount)
        
# obj = ATM()
# obj.deposit(2500)
# obj.withdraw(300)
# obj.check_bal()




# Inheritance
# class Car:
#     def __init__(self, name):
#         self.name = name
        
#     def __str__(self):
#         return self.name


# class Maruti(Car):
#     def __init__(self, name, model):
#         Car.__init__(self, name)
#         self.name = name
#         self.model = model
    
#     def __str__(self):
#         return super().__str__()
        
# new_obj = Maruti("Dezire", 2024)
# print(new_obj)






