menu = {
        "cholle bhature" : 180, 
        "pizza": 150,
        "sandwich": 80,
        "burger" : 50
        }
 
def Restorent():
    item = "y"
    order1 = input("Enter Your Order : ")
    ans =  menu.get(order1)
    print(f'Current amount: {ans}')
    item_entered = 1
    while item == "y":
        item = (input('Enter more (y/n): '))
        while item not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            item = (input('Enter more (y/n): '))
            
        if item == 'n':
            break
        order = input("Enter Your Order : ")
        ans+=menu.get(order)
        print(f'Current amount: {ans}')
        item_entered+=1
    return[ans,item_entered]        


def orderd():
    flag = True
    while flag:
        num = int(input('''
        <-------Welcome To Bhopal Restaurants------->
                    ----Your Choices Is----
                    
            1. The Public Restaurant       --> (Enter : 1)
            2. Good Food Restaurant        --> (Enter : 2)      
            3. Saffron Restaurant          --> (Enter : 3)  
            4. Manohar Restaurant          --> (Enter : 4)
                          
            Enter Number 2 For EXIT   
            Enter Your Choise : '''))
        
        if num == 1:
            num1 = int(input('''
                    *-----MENU-----*
            __________________________________
                         
                1. cholle Bhature  ₹ 180
                2. Pizza           ₹ 150
                3. sandwich        ₹  80
                4. Burger          ₹  50
            ___________________________________       
                Enter Number 1 For Order
                Enter Number 2 For Back
                Enter Your Choice : '''))
            
            if num1 == 1:
                results = Restorent()
                print('Total Amount :',results[0],'₹', 'total item :',results[1],"\n")
            elif num1 == 2:
                continue

orderd()
            