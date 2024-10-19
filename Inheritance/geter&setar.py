# class Student:
#     def __init__(self):
#         # self.__name=""
#         self.a = None
#         self.b = None

#     def getname(self):
#         return self.a + self.b
    
#     def setname(self,a,b):
#         # self.__name = name
#         self.a = a
#         self.b = b

# obj = Student()
# obj.setname(5,5)
# name = obj.getname()
# print(name)

class Car:
    def __init__(self, name):
        self.name = name
        # self.lname = lname
        
    def __str__(self):
        return self.name


class Maruti(Car):
    def __init__(self, name):
        Car.__init__(self, name)
        self.name = name
        # self.model = model
    
    def __str__(self):
        return super().__str__(self)

        
new_obj = Maruti("Dezire")
print(new_obj)
