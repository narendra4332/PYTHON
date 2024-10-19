my_tuple = tuple()
print("*======Welome TO MY Tuple Function======*")
flag = True
while flag:
    num = int(input('''
                1 For Add Element
                2 For Check Min Element 
                3 For Check Max Element
                4 For count Any Element
                5 For sum Of All Element In Tuple
                6 For Check index Of Any Value
                7 For Add number from 1 To 10
                8 For exit.

                    '''"Enter Your Choice :-"))
    if num == 1:
        for element in range(1,5):
            number = int(input("\nEnter Number which you want to Add: "))
            new_tuple = list(my_tuple)
            new_tuple.append(number)
            my_tuple = tuple(new_tuple)
            print("Added Elements In Tuple: ",my_tuple)
    elif num == 2:
        print("\nThis Is Min Number :",min(my_tuple))
    elif num == 3:
        print("\nThis Is Max Number :",max(my_tuple))
    elif num == 4:
        number = int(input("Enter Any Number"))
        a = my_tuple.count(number)
        print("\n"f'The Number {number} Is:  {a} Times In Tuple')
    elif num == 5:
        sum_tpl = sum(my_tuple)
        print("\nThe Sum Is: ",sum_tpl)
    elif num == 6:
        number = int(input("Enter Any Number"))
        b = my_tuple.index(number)
        print("\n"f'Index Of {number} Number Is: {b}')
    elif num == 7:
        num1 = 1
        while num1<=11:
            new_tuple = list(my_tuple)
            new_tuple.append(num1)
            num1 = num1 + 1
            my_tuple = tuple(new_tuple)
        print(my_tuple)
        
    elif num == 8:
        flag = False
    else:
        print("INVALID NUMBER...!")



