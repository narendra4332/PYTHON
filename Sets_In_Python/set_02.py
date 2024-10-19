this_set = set()
flag = True
while flag:
    number = int(input('''
                1 add
                2 discard
                3 pop 
                4 clear
                5 remove
                6 exit                           
                       '''))
    if number == 1:
        if number == 0:
            print("INVALID NUMBER..!")
        else:
            num = int(input("Enter any value"))
            this_set.add(num)
            print(this_set)
    elif number == 2:
        num = int(input("Enter any value"))
        this_set.discard(num)
        print(this_set)
    elif number == 3:
        this_set.pop()
        print(this_set)
    elif number == 4:
        this_set.clear()
        print(this_set)
    elif number == 5:
        num = int(input("Enter any value"))
        this_set.remove(num)
        print(this_set)
    elif number == 6:
        flag = False
    else:
        print("INVALID NMBER..!")

        



        
        
                
        