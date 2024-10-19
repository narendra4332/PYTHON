# Print all items in the list, one by one:

# number_list=["one","two","three","four","five","six"]
# for x in number_list:
#     print(x)

# Use the range() and len() functions to create a suitable iterable.

# number_list=["one","two","three","four","five","six"]
# for x in range(len(number_list)):
#     print(number_list[x])

 # Print all items, using a while loop to go through all the index numbers

# num_list=[11,45,65,23,75,44]
# i=0
# while i <len(num_list):
#     print(num_list[i])
#     i=i+1

# A short hand for loop that will print all items in a list:

# city_list=["bolpal","vidisha","jaipur","banglore"]
# [print(x) for x in city_list]


# city_list=["bolpal","vidisha","jaipur","banglore","red","blue"]
# new_list=[]

# for x in city_list:
#     if "i"in x:
#         new_list.append(x)  
# print(new_list)

# With list comprehension you can do all that with only one line of code:
# city_list=["bolpal","vidisha","jaipur","banglore","red","blue"]
# new_list =[x for x in city_list if "i" in x]
# print(new_list)


# # You can use the range() function to create an iterable:

# my_list=[x for x in range(10) if x<5]
# print(my_list)

# # Set the values in the new list to upper case:
# city_list=["bolpal","vidisha","jaipur","banglore","red","blue"]

# list_item=[x.upper() for x in city_list]

# print(list_item)

name =[x for x in range('a'-'z')]
print(name)







