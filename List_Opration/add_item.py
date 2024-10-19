# To add an item to the end of the list, use the append() method:

colorlist=["red","blue","orange"]
colorlist.append("white")
print(colorlist)

# The insert() method inserts an item at the specified index:

subjectlist = ["math","science","hindi"]
subjectlist.insert(1,"english")
print(subjectlist)

# To append elements from another list to the current list, use the extend() method.

colorlist=["red","blue","orange"]
subjectlist = ["math","science","hindi"]
colorlist.extend(subjectlist)
print(colorlist)

# Add elements of a tuple to a list:
this_list =["apple","banana","chery"]
this_tuple =("kiwi","orange")
this_list.extend(this_tuple)
print(this_list)















