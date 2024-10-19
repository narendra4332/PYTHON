# 11.Question: Write a function to check if a string is a palindrome.

# def palindrome(a):
#     result = a[::-1]
#     print(result)
#     if result == a:
#         print(True)
#     else:
#         print(False)

# palindrome("racecar")

# Question: Write a function to calculate the factorial of a number

# def factorial(number):
#     fact = 1
#     for i in range(1,number+1):
#         fact = fact*i
#     print(fact)

# factorial(5)

# 13.Question: Write a function to merge two sorted lists into one sorted list. ??????????
# merge_sorted_list=[1, 3, 5]
# marge_sorted_list1=[2, 4, 6]
# new = merge_sorted_list+marge_sorted_list1
# new.sort()
# print(new)

# 14.Write a function to find the greatest common divisor (GCD) of two numbers.
# def GCD(num1,num2):
#     for i in range(2,100):
#         if num1 % i == 0 and num2%i == 0:
#             ans = i
#     print("Greatest Common Divisor Is : ",ans)

# GCD(27,18)

# 15.Question: Write a function to reverse a string.

# def Reverse(name):
#     result = name[::-1]
#     print(result)

# Reverse("narendra")

# 17.Write a function to find the second largest number in a list.
# my_list = []
# for i in range(int(input("Enter Element Which You Want To Add In List : "))):
#     add = int(input("Enter Element : "))
#     my_list.append(add)

# def Second_max(my_list):
#     my_list.sort()
#     print("Second Largest Number Is : ",my_list[-2])
# Second_max(my_list)


# 18.Question: Write a function to count the number of vowels in a string.

# def Num_vowels(name):
#     count = 0
#     count1 = 0
#     for i in name:
#         if i == "a" or i == "e" or i=="i" or i=="o" or i=="u":
#             count+=1
#         else:
#             count1+=1
#     print("Number Of Vowels Is :",count)
#     print("Number Of Consonent Is:",count1 )

# Num_vowels("abcdefghijklmnopqrstuvwxyz")

# 19.Question: Write a function to check if a given year is a leap year.

# def leap_year(year):
#     if year%100 == 0 and year%400 == 0:
#         print(True)
#     elif year%4 == 0 and year%100 !=0:
#         print(True)
#     else:
#         print(False)

# leap_year(2020)

# Question: Write a function to convert a decimal number to binary.
# def convertToBinary(n):
#    if n > 1:
#        convertToBinary(n//2)
#    print("Binary Number Is : ",n % 2,end = '')

# convertToBinary(34)


# second_larges=([3, 1, 4, 1, 5, 9])
# second_larges.sort(reverse=True)
# print(second_larges[1])


    # i = i[0:2]
    # print(i)


# name = {
#     "a":1,
#     "d":5,
#     "c":9
# }

# new = list(name.items())
# print(new)
# new.sort()
# print(new)
# new1 = dict(new)
# print(new1)
