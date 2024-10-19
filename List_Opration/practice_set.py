number_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
new_list1=[]
for i in number_list:
    if i%2==0:
      new_list.append(i)
    elif i%2!=0:
      new_list1.append(i)

print(new_list)
print(new_list1)

# =============

number_list=[1,2,3,4,5,6,7,8,9,10]
newlist=[]
even_list=[x for x in number_list if x%2==0]
print(even_list)

# ================

# number = 1
# first_list=[]
# secon_list=[]
# while number<50:
#     if number%2==0:
#         first_list.append(number)
#     if number%2!=0:
#         secon_list.append(number)
#     number=number+1
# #    print(number)
# print("1 To 50 EVEN NUMBER:\n",first_list)
# print("1 To 50 Odd NUMBER:\n",secon_list)
