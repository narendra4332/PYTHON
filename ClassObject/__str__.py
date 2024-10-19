# string representation of an objectwithout __str__() function

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("narendra",21)
print(p1)

# string representation of an objectwith __str__() function

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"
    
p1 = Person("narendra",21)
print(p1)



      
      
      


