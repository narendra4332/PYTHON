# class DenoClass:
#     a  = 10

#     def  sumvalue(self):
#         print(20+30)

# demoobject = DenoClass()
# demoobject1 = DenoClass()
# print(demoobject.a)
# print(demoobject1.a)
# demoobject.sumvalue()

# ===================================================

class DemoClass:
    name = "narendra"
    value = 20

    def __init__(self):
        print("hello how are you")
        self.c = self.value+self.value
        print(self.c)
    

    def __init__(self,a,b):
         self.c = a+b
         print("sum = ",self.c)


        

# __init__ is a constractor ye apne aap call hota ise hame call nhi karna padta 

    def showvalue(self):
        print(self.name)
        self.sum = self.value + self.value
        print(self.sum)

    def showvalue1(self, a,b):
        print(a+b)
        print("hi my name is narendra lodhi")


obj = DemoClass(int(input("Enter first Number: ")),
int(input("Enter second number: ")))
obj.showvalue()
obj.showvalue1(10,20)

# ==================================================================

