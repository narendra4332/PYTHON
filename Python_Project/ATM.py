# flag = True
# while flag:
#     number= int(input('''
#                If You Want To Diposit Mouny Plese Enter Number 1 
#                If You Want To Withdrowl Mouny Plese Enter Number 2
#                If You Want To exit please Enter Number 3                                       
#                Enter Your Choise : '''))

# class Atm:
#         def __init__(self,id,name):
#             self.id = id
#             self.name = name
#             self.bal = 0.0

#         def Diposit(self,amount):
#             self.bal += amount
#             print("DEPOSIT DONE : ₹",self.bal)

#         def withdrowl(self, wd_amount):
#             if self.bal>=wd_amount:
#                 self.bal-=wd_amount
#                 print("WITHDRAWL DONE : ₹",self.bal)
            

#         def CheckBalance(self):
#             print("TOTAL BALANCE IS ₹",self.bal)
 
# obj = Atm(142,"narendra")
#     # if number == 1:
#     #     obj.Diposit((int(input("\nPlese Enter How Much Mony Do You Want To Diposit :"))))
#     #     obj.CheckBalance()
#     # elif number == 2:
#     #     obj.withdrowl((int(input("\nPlese Enter How Much Mony Do You Want To Withdrowl :"))))
#     #     obj.CheckBalance()
#     # elif number == 3:
#     #     flag = False

# obj.Diposit(1000)
# obj.CheckBalance()
# obj.withdrowl(500)
# obj.CheckBalance()



class Atm:
    def __init__(self, id,name):
        self.id = id
        self.name = name
        self.balance = 0.0

    def Diposit(self,amount):
        self.balance+=amount
        print("Diposit Done : ₹",self.balance)
    
    def Withdrowl(self,amount1):
        if self.balance>=amount1:
            self.balance-=amount1
            print("Withdrowl Done : ₹",amount1)
        else:
            print("Insufficiens bal")

    def Check_balance(self):
        print("Total Balance : ₹",self.balance)

flag = True
while flag:
    number = int(input('''
        1 For Diposit Mouny 
        2 For Withdrowl Mouny
        3 For Exit 
        Enter Your Choise :'''))
    
    if number == 1:
        obj = Atm(123,"Narendra")
        obj.Diposit(int(input("How Much Mony Do You Want To Diposit:")))
        obj.Check_balance()
    elif number == 2:
        # obj.Check_balance()
        obj.Withdrowl(int(input("How Much Do You Want To Withdrowl : ")))
        obj.Check_balance()
    elif number == 3:
        flag = False