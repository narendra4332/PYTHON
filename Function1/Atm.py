class Atm:
    def __init__(self, id , name):
        self.id=id
        self.name=name
        self.bal=0.0

    def diposit(self, amount):
        self.bal += amount
        print("diposit Done")


    def withdrowl(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else:
            print("insufficient")

    def Check_balance(self):
        print(self.bal)

operation = input("if you want to diposit amount plese inter number:1\n\nif you want to withdrowl amount plese enter number:2\n\nif you want to check balance pese enter number:3\n\nenter number:")


narendra = Atm(123, "narendra")

if int(operation) == 1:
    amount =  float(input("\nPlese enter amount:"))
    print(f"{narendra.diposit(amount)}")

elif int(operation) == 2:
    amount =  float(input("\nPlese enter amount:"))
    print(f"{narendra.withdrowl(amount)}")

elif int(operation) == 3:
    print(f"{narendra.Check_balance()}")

else:
    print("INVALID NUMBER !")
