# 21.Write a function to flatten a nested list.

# flatten_list = ([[1, 2, 3], [4, 5]])

# def flatten(flatten_list):
#     flat = []
#     for sublist in flatten_list:
#         for num in sublist:
#          flat.append(num)
#     print(flat)

# flatten(flatten_list)

# 23.Question: Write a function to check if a string contains only unique characters.
# def unique_characters(st):
#     x=list(set(st))
#     y=list(st)
#     x.sort()
#     y.sort()
#     if(x==y):
#         print(True)
#     else:
#         print(False)
# unique_characters("abcd")

# Question: Write a function to rotate a list by k elements.
# roted_list = [1,2,3,4,5]
# def roted(roted_list):
#     roted_list = roted_list[3:] + roted_list[:3]
#     print("Roted List = ",roted_list)
# roted(roted_list)

# 25.Question: Write a function to find the intersection of two lists.
# list_intersection = [1, 2, 3] 
# list_intersection1 = [2, 3, 4]
# def intersection(list_intersection, list_intersection1):
#     x = set(list_intersection) & set(list_intersection1)
#     y = list(x)
#     print(y)
# intersection(list_intersection,list_intersection1)

# 26.Write a function to implement a basic calculator that can add, subtract, multiply, and divide.

# def basic_calculator(num1,num2):
#     print("Addition = ",num1 + num2)
#     print("Subtraction = ",num1 - num2)
#     print("Multiplication = ",num1 * num2)
#     print("Division = ",num1 / num2)

# basic_calculator(24,8)

# Fibonacci number
# num1 = 0
# num2 = 1

# print(num1)
# print(num2)
# for fibo in range(10):
#     newFibo = num1 + num2
#     print(newFibo)
#     num1 = num2
#     num2 = newFibo


# element_frequency = [1, 2, 2, 3, 3, 3,1,1]

# fequency = {}

# for item in element_frequency:
#     if item in fequency:
#         fequency[item] += 1
#     else:
#         fequency[item] = 1
# print(fequency)
    

def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx
print(newtonsqrt(16))