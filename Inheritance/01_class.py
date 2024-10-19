# # Inheritance 
# # (1) Single inheritance (2) multilevel inheritance (3) multiple inheritanse

# class A:
#     def displayA(self,a,b):
#         print(a+b)

# class B(A):
#     def displayB(self,c,d):
#         print(c-d)

# class C(B):
#     def displayC(self,e,f):
#         print(e*f)



# obj = C()
# obj.displayA(10,20)
# obj.displayB(10,5)
# obj.displayC(5,5)


# import random
# import math
# upper = 1
# lower = 10 
# number = random.randint(1, 10)
# total_chances = math.ceil(math.log(upper - lower+1,2))

# print(number)


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
# obj.withdraw(3000)
# obj.check_bal()




# Inheritance
class Car:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


class Maruti(Car):
    def __init__(self, name, model):
        Car.__init__(self, name)
        self.name = name
        self.model = model
    
    def __str__(self):
        return super().__str__()

        
new_obj = Maruti("Dezire",2024)
print(new_obj)
























