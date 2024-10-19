my_arry = []

while True:
    number = int(input('''
                    1 For Adds an element at the end of the list
                    2 For remove all element from arry
                    3 For Returns a copy of the list
                    4 For count Returns the number of elements with the specified value
                    5 For Returns the index of the first element with the specified value
                    6 For Removes the element at the specified position
                    7 For Removes the first item with the specified value
                    8 For Reverses the order of the list
                    9 Break 
                    Entet Your Choice : '''))
    def Add(num):
        for element in range(1,10):
            my_arry.append(element[num])
            print(my_arry)

    def Remove():
         my_arry.clear()
         print(my_arry)

    def Copy():
        my_arry.copy()
        print(my_arry)
    
    def Count(num):
        new_arry = my_arry.count(num)
        print(new_arry)

    def Return():
        num = input("\nEnter element which you want to return :")
        new_arry = my_arry.index(num)
        print(new_arry)

    def remove_index_value():
        num = input("\nEnter index which you want to remove :")
        my_arry.pop(num)
        print(my_arry)

    def remove_value():
        num = input("\nEnter value which you want to remove :")
        my_arry.remove(num)
        print(my_arry)

    def reverse():
        my_arry.reverse()
        print(my_arry)

    
    if number ==  1:
        Add(num = input("\nEnter element which you want to add :"))
        Add(num = input("\nEnter element which you want to add :"))
        Add(num = input("\nEnter element which you want to add :"))
    elif number == 2:
        Remove()
    elif number == 3:
        Copy()
    elif number == 4:
        Count(num = input("\nEnter element which you want to count :"))
        Count(num = input("\nEnter element which you want to count :"))

    elif number == 5:
        Return()
    elif number == 6:
        remove_index_value()
    elif number == 7:
        remove_value()
    elif number == 8:
        reverse()
    elif number == 9:
        break




