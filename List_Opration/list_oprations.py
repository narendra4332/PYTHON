this_list=[]
flag = True
while flag:
    c = int(input('''
            1 Push Elements
            2 Pop Elements
            3 Peek Ekement.
            4 Disply Stack
            5 Insert Element On Index 0
            6 Remove Elemet
            7 Copy List Eliments
            8 Count Elements
            9 Reverse The List
            10 Remove Duplicate Elements
            11 Chang First List Item
            12 Add Any five Faivreit Color
            13 Add Number From 1 To 10
            14 Add Even Number In List From 1 To 10
            15 Exit
                    
            '''"Enter Your Choice: "))
    if c == 1:
        n=input("\nEnter The Value: ")
        this_list.append(n)
        print(this_list)
    
    elif c == 2:
        if len(this_list)==0:
            print("\nEmpty List: ")
        else:
            p=this_list.pop()
            print(p)
            print(this_list)

    elif c == 3:
        if len(this_list)==0:
            print("\nEmpty List: ")
        else:
            print("\nLast stack Value: ",this_list[-1])
    elif c == 4:
        print("\nDisplay Stack: ",this_list)

    elif c == 5:
        if len(this_list)==0:
            print("\nEmpty List: ")
        else:
            n=input("\nEnter The Value: ")
            this_list.insert(0,n)
            print(this_list)

    elif c == 6:
        if len(this_list)==0:
            print("\nEmpty List: ")
        else:
            n=input("\nEnter The Value: ")
            this_list.remove(n)
            print(this_list) 
    elif c == 7:
        this_list.copy()
        print("\nCopy List",this_list)  
    elif c == 8:
        n=input("\nEnter The Value: ")
        new_list=this_list.count(n)
        print(f'{n} number is: {new_list} Times')
    elif c == 9:
        this_list.reverse()
        print("\n Reverse List: ",this_list)
        
    elif c == 10:
        this_list = list(dict.fromkeys(this_list))
        print(this_list)
    elif c == 11:
        n=input("\nEnter The Value: ")
        this_list[0]=(n)
        print(this_list)
    elif c == 12:
        for element in range(1,5):
            color = input("\nEnter your faivret colors "+str(element)+":")
            this_list.append(color)
        print("\nFaivret Color:-",this_list)
    elif c == 13:
        num = 1
        while num<11:
            this_list.append(num)
            num = num+1
        print("\nAdd Number:",this_list)
    elif c == 14:
        num = 1
        while num<11:
            if num%2==0:
             this_list.append(num)
            num = num+1
        print("\nEven Number:",this_list)    
    elif c == 15:
        flag = False
    else:
        print("INVALID NUMBER!")
        