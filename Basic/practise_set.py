# Method 1: Sorting the list and then printing the elements of the second last index
# declaring the list
lst = []
for i in range(int(input("Enter the number of elements to enter in the list: "))):
    x = int(input("Enter the element: "))
    lst.append(x)

def method1(lst):
    lst.sort()     # sorting the list
    print("The second largest element of the list is: ", lst[-2])     # printing the element of the second last index

method1(lst) # calling the function
