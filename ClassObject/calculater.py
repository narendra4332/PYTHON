class Calculater:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def Add(self):
        return self.x + self.y
    def Sub(self):
        return self.x - self.y
    def Mul(self):
        return self.x * self.y
    def Divi(self):
        return self.x / self.y

x = int(input("Enter 1:"))
y = int(input("Enter 1:"))    
obj = Calculater(x,y)
obj1 = obj.Add()
print("Addition =",obj1)
obj2 = obj.Sub()
print("Subtraction =",obj2)
obj3 = obj.Mul()
print("Multiplication =",obj3)
obj4 = obj.Divi()
print("Division =",obj4)