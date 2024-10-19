# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def Speak(self):
#         return f"{self.name} says "
    
# class Dog(Animal):
#     def Speak(self):
#         return f"{super().Speak()}{"Woof !"}"

# class Cat(Animal):
#     def Speak(self):
#         return f"{super().Speak()}{"Meow !"}"
    
# class Cow(Animal):
#     def Speak(self):
#         return f"{super().Speak()}{"Amma !"}"
    
# obj = Dog("Dog")
# obj1 = Cat("Cat")
# obj2 = Cow("Cow")
# print(obj.Speak())
# print(obj1.Speak())
# print(obj2.Speak())


class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        self.num = self.num1+self.num2
        return f"Additon = {self.num}"
#         return f"{super().Speak()}{"Amma !"}"


    



num1 = Calculator(float(input("Enter First Number : ")),float(input("Enter Second Number : ")))
print(num1)


# sub = Subtraction(5,2)
# print(sub)




        

