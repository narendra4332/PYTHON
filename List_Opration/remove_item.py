# The remove() method removes the specified item.

phone_list = ["apple","nokia","oppo","vivo"]
phone_list.remove("oppo")
print(phone_list)

# If there are more than one item with the specified value, the remove() method removes the first occurance:
phone_list = ["apple","nokia","oppo","vivo","oppo"]
phone_list.remove("oppo")
print(phone_list)

# The pop() method removes the specified index.

number_list=["one","two","three","four"]
number_list.pop(1)
print(number_list)

# If you do not specify the index, the pop() method removes the last item.

number_list=["one","two","three","four"]
number_list.pop()
print(number_list)

# The del keyword also removes the specified index:

# bick_list=["hero","ninja","sujuki","yama"]
# del bick_list[1]
# print(bick_list)

# The clear() method empties the list.
# Clear the list content:

# num_list=[1,2,3,4,5,6]
# num_list.clear()
# print(num_list)


















