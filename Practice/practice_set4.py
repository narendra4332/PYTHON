class Student:
    def __init__(self,name,brance):
        self.name = name
        self.brance = brance

    def __str__(self):
        return f"Your Name Is {self.name}, cand Your Brance Is {self.brance}"
    

class Collage(Student):
    def __init__(self,name,brance,corse):
        self.corse = corse
        super().__init__(name,brance)

    def __str__(self):
        return f"{super().__str__() }, cand Your corse is {self.corse}"

class Collage1(Collage):
    def __init__(self,name,brance,corse,age):
        self.age = age
        super().__init__(name,brance,corse)

    def __str__(self):
        return f"{super().__str__() }, your age is {self.age}"


obj = Collage1("narendra","cse","b.tech",22)
print(obj)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age} years old"

# class LibraryItem:
#     item_count = 0  # Class variable

#     def __init__(self, title, year):
#         self.title = title
#         self.year = year
#         LibraryItem.item_count += 1

#     def __str__(self):
#         return f"{self.title} ({self.year})"

# class Author(Person):
#     def __init__(self, name, age, books_written):
#         super().__init__(name, age)
#         self.books_written = books_written  # List of book titles

#     def __str__(self):
#         books = ', '.join(self.books_written)
#         return f"{super().__str__()} - Author of: {books}"
    

# obj = Author("narendra",22,["1212","myname","hello"])
# print(obj)
