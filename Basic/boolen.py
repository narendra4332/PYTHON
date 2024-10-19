# txt = "hello mu name is \"narendra\" "
# print(txt)

# txt = "hello\' how are you"
# print(txt)

# txt = "this will insert one \\(backslash)"
# print(txt)

# # boolen 
# # you can evaluate any expression in pytho and get one of two answers, true or false
# print(10>9)
# print(10==9)
# print(10<9)

# a=10
# b=33
# if b>a:
#     print("\"b\" is grester than \"a\"")
# else:
#     print(" \"b\" is not greater than \"a\"")


# #TRUE
# x= "hello"
# y=15
# print(bool(x))
# print(bool(y))
# print(bool("abc"))
# print(bool(123))
# print(bool([1,2,3,4,5,6]))

# #FALSE
# print(bool())
# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool({}))

# # function can return a boolen

# # def myFunction():
# #     return True
# # print(myFunction())


# def myFunction1():

#     return True



# if myFunction1():
#     print("YES")
# else:
#     print("NO")

# x = 200
# print(isinstance(x, int))

# def add(a,b):
#     sum = a+b
#     lst=[]
#     lst.append(sum) 
#     print(lst)

# add(10,20)
# add(20,30)
# add(40,50)

# important ---------------

# my_list = [1,2,3,5,6]
# target = 7
# n = len(my_list)
# for i in range(n - 1):
#     # print(my_list[i])
#     for j in range(i + 1, n):
#         print(my_list[j])
# #         if my_list[i] + my_list[j] == target:
# #             print([i, j])
# # # print() # No solution found

# my_list = [1,6,5,3,4]
# max = my_list[0]
# for i in my_list:
#     if i > max:
#         max=i
# print(max)
# my_set = (0)
# for i in my_list:
#     if i>my_set:
#         my_set = i
# print(my_set)

# if num == 1:
#             num3 = int(input('''
#         **HOW MANY DAY DO YOU WANT TO BOOK HOTEL**
#                 AMOUNT IS : 250₹ PAR DAY                
#             Plese Enter Your DAY : '''))
num3 = 4
amount = 0
if num3>=1:
    for element in range(0,num3):
        amount += 250
        print(amount)















