mydict = {

}
flag = True
while flag:
    client = int(input('''
                    1. Add Element in dict.
                    2. Get The Value From dict.
                    3. Get All keys From Dict.
                    4. Get All Values From Dict.
                    5. Get All keys And Value From Dict.
                    6. Update Data in Dict.
                    7. Delet Value From Key.
                    8. POP Item. 
                    9. clear Dict.
                    10 Exit
                       
                    Enter Your Choise:  '''))
    if client ==1:
        name =  input("Enter Any Key Which You Want to Add In Dict: ")
        name1 = input("Enter Any Value Which You Want to Add In Dict: ")
        mydict[name]=name1
        print(mydict)

    if client == 2:
        name = input("Enter key name which value you want to get: ")
        print("\n",mydict.get(name))

    if client == 3:
        for element in mydict.keys():
            print(element)

    if client == 4:
        for element in mydict.values():
            print(element)
    
    if client == 5:
        for element1,element2 in mydict.items():
            print(element1,':',element2)

    if client == 6:
        name =  input("Enter Key Which You Want to Update In Dict: ")
        name1 = input("Enter Value Which You Want to Add In Dict: ")
        mydict.update({name:name1})
        print(mydict)

    if client == 7:
        name = input("Enter The key Which You Want to delet: ")
        del mydict[name]
        print(mydict)

    if client == 8:
        name = input("Enter The key Which You Want to POP: ")
        print("It has poped this value: ",mydict.pop(name))

    if client == 9:
        print(mydict.clear())
    
    if client == 10:
        flag = False


    


    
        


