my_list = []
flag = True
while flag:
    number = int(input('''
1 For Add Element
2 For Remove Element
3 For Access Thired Element
4 For Largest Number
5 For Remove Duplicate
6 For Iterate Each Element
7 For Count Number 
8 For Accending Orderd List 
9 For Merge A List
10 For Exit 
                                   
Enter Your Choise : '''))
    
    def Add(num):
        my_list.append(num)
        print("Added Element Is :",my_list)

    def Remove(num):
        my_list.remove(num)
        print(num,"Has Removed Form LIst :",my_list)

    def Access():
        print("The Value In Index 3 Is : ",my_list[2])

    def LargrNumber():
        max = my_list[0]

        for i in my_list:
            if i>max:
                max = i
        print("Max Number Is : ",max)

    def RemoveDuplicate():
        this_list = list(dict.fromkeys(my_list))
        print("Duplicate Number's Has Removed",this_list)

    def Iterate():
        for element in my_list:
            print(element)

    def CountNumber(num):
        new_list = my_list.count(num)
        print(num," Is ",new_list," Times In List")
    
    def AccendingOrderd():
        my_list.sort()
        print("List In Accending Orderd :",my_list)

    def MergeList():
        this_list = ["red","black","White"]
        my_list.append(this_list)
        print("Merge List Is :",my_list)
    
    if number == 1:
        Add(int(input("Enter Element Which you Want to Add : ")))
    elif number == 2:
        Remove(int(input("Enter Element Which You Want To Remove :")))
    elif number == 3:
        Access()
    elif number == 4:
        LargrNumber()
    elif number == 5:
        RemoveDuplicate()
    elif number == 6:
        Iterate()
    elif number == 7:
        CountNumber(int(input("Enter Element Which You Want to Count : ")))
    elif number == 8:
        AccendingOrderd()
    elif number == 9:
        MergeList()
    elif number == 10:
        flag = False
    else:
        print("INVALID NUMBER !")
    




    
    
    
