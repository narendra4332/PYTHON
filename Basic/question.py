# for element in range(1,50+1):
#     if element%2==0:
#         print(element)

# for element in range(1,50+1):
#     if element%2==0:
#         continue
#     else:
#         print(element)

# ***********************************

# mylist = [10,20,30,40,50]
# mylist.remove(10)
# print(mylist)

# for elment in range(len(mylist)):
#     if mylist[elment] == 10:
#         continue
#     print(mylist[elment])

# ***********************************

name = "yyyYYYyySSSsssrRRrrrTTTttt"


# my_dict = {}

# for i in name:
#     if i.lower() not in my_dict.keys() and i.upper() not in my_dict.keys():
#         my_dict[i] = True

# ans = ''

# for j in my_dict.keys():
#     ans += j

# print(ans)

# =========================================


# my_list = [10,34,5,67,8,2,9]
# max = my_list[0]

# for i in my_list:
#      if i > max:
#         max = i
# print(max)

# ===========================================
# my_list = [5,2,3,6,1]
# target = 7
# n = len(my_list)
# for i in range(n - 1):
#     print(my_list[i])
#     for j in range(i + 1, n):
#         print(my_list[j])
#         if my_list[i] + my_list[j] == target:
#             print((i, j))

# ==============================================

# my_list = [1,1,2,2,4]
# my_set = set()
# for i in my_list:
#     if i in my_set:
#         print(i)
#     else:
#         my_set.add(i)

# ==============================================

str = "yesi lagi lagan mira ho gai magan"

str1 = {}

for x in str:
    if x in str1:
        str1[x] +=1
    else:
        str1[x] = 1
print(str1)
      


        


        
        
