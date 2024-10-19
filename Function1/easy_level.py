# 1.Question: Write a function to check if a number is even.

# def Even(number):
#     if number%2 == 0:
#         print(True)
#     else:
#         print(False)

# Even(int(input("Enter Any Number : ")))

# 2.Question: Write a function to convert Celsius to Fahrenheit.

# def Celsius_Fahrenheit(celsius):
#     fahrenheit = (celsius*1.8)+32
#     print("Fahrenheit Is : ",fahrenheit)

# Celsius_Fahrenheit(int(input("Enter Temperature in celsius : ")))

# 3.Question: Write a function to find the maximum of three numbers.
# Sample Input: max_of_three(1, 5, 3)
# Expected Output: 5
# (1)
# def myMax(x,y,z):
#     if (x>=y) and (x>=z):
#         print("Largest Number Is : ",x)
#     elif (y>=x) and (y>=z):
#         print("Largest Number Is : ",y)
#     else:
#         print("Largest Number Is : ",z)

# myMax(8,5,4)

# (2)
# mylist = [1,5,12,8,34]
# max = mylist[0]

# for i in mylist:
#     if i > max:
#         max = i
# print("max number is :",max)

# 4.Question: Write a function to calculate the area of a circle given its radius.

# def findArea(r):
#     pi = 3.142
#     area = pi*(r*r)
#     print("Area Is : ",area)

# findArea(4)
        
# 5.Question: Write a function to remove all vowels from a string.

# def RemoveVowels(name):
#     vowels = ["a","e","i","o","u","A","E","I","O","U"]
#     result = ""
#     for i in range(len(name)):
#         if name[i] not in vowels:
#             result = result+name[i]
#     print(result)

# RemoveVowels("narendra lodhi ")

# (2)
# def Vowels(name):
#     result = ""
#     for i in name:
#         if i=="a" or i == "e" or i=="i" or i=="o" or i == "u":
#             pass
#         else:
#             result = result+i
#     print(result)
# Vowels("narendra")


# 6.Question: Write a function to count the number of words in a sentence.

# def CountWord(name):
#     count = 1
#     for i in name:
#         if i == " ":
#             count+=1
#     print(count)
    
# CountWord("narendra lodhi")

# 7.Question: Write a function to check if a number is positive, negative, or zero.

# def Check_Number(x):
#     if x < 0:
#         print(x,"is negative")
#     elif x > 0:
#         print(x,"is positive")
#     else:
#         print(x,"is zero")

# Check_Number(2)

# 8.Question: Write a function to return the square of a number.

# def My_square(number):
#     square = number*number
#     print("square_root of",number,"is : ",square_root)
# My_square(4)

# 9.Question: Write a function to find the sum of all elements in a list.

# def Sum_List():
#     sum = 0
#     My_list = [1,2,3,4,5]
#     for i in My_list:
#         sum = sum+i
#     print(sum)
# Sum_List()

# 10.Question: Write a function to find the length of a string.
# def fin_length(name):
#     print(len(name))
# fin_length("hello")
     