def Bus_ticket(number,number1):
        global bus_ticket

        if number == "indore" and number1 == "bhopal" or number=="bhopal" and number1 == "indore" or number == "vidisha" and number1 == "jawalpur" or number == "jawalpur" and number1 == "vidisha":
                bus_ticket= 100
                print("\nYour Bus Ticket Is : ₹",bus_ticket,"Par Person")

        elif number == "indore"and number1=="vidisha" or number=="vidisha" and number1 == "indore" or number == "bhopal" and number1 == "vidisha" or number == "vidisha" and number1 == "bhopal":
                bus_ticket = 200
                print("\nYour Bus Ticket Is : ₹",bus_ticket,"Par Person")

        elif number == "indore" and number1 == "jawalpur" or number == "jawalpur" and number1 == "indore" or number=="bhopal" and number1=="jawalpur" or number=="jawalpur" and number1=="bhopal":
                bus_ticket = 300
                print("\nYour Bus Ticket Is : ₹",bus_ticket,"Par Person")
        else:
              print("INVALID CHOICE !")
    
def Person(person_number):
        global person
        global amount
        person = person_number
        amount = 0
        if person_number>=1:
            for element in range(0,person):
                amount += bus_ticket
            print("\nYour Total Amount Is : ₹",amount)
     
def Hotel(days):
        global total1
        amount1 = 0
        amount2 = 0
        hotel_rent = 250
        if days>=1:
            for element in range(0,days):
                    amount1 += hotel_rent
                    total = amount1
            for element in range (0,person):
                    amount2 += total 
                    total1 = amount2 + amount
            print("\nYour Total Amount Is : ₹",total1)

def Return_ticket(): 
        ticket = total1 + amount
        print("\nYour Total Amount Is: ₹",ticket)
        
        
flag = True
while flag:
    choice = int(input('''
            <=====-------WELCOME TO MY PROJECT-------======>      
            <-----WHEAR DO YOU WANT TO GO YOUR CHOICES IS----->
                                1. INDORE
                                2. BHOPAL
                                3. VIDISHA
                                4. JAWALPUR
                        Enter Number 1 For Start 
                        Enter Number 2 For Exit            
                        Enter Your Choice :  '''))

    if choice == 1: 
        Bus_ticket(input("\nPlese Enter Your Starting Point : "),input("Plese Enter Your Ending Point : "))
    elif choice == 2:
          break
    else:
          print("INVALID CHOICE !")
          continue

    Person(int(input("\nEnter Number Of Persion : ")))


    choice1 = int(input('''
                <----Do You Want To Book Hotel---->
            <-Hotel Amount Is ₹ 250 Par Day Par Person->
                        1 For Yes 
                        2 For No
                        Enter Your Choice : '''))
                            
    if choice1 == 1:
        Hotel(int(input("Plese Enter Your Days : ")))
    elif choice1 == 2:
        print("\nYour Total Amount Is : ₹",amount)


    choice2 = int(input('''
            <----Do You Want To Return Your Ticket---->
                        1 For Yes
                        2 For No
                        Enter Your Choise :'''))
    if choice2 == 1 and choice1 == 1:
        Return_ticket()
    elif choice2 == 2 and choice1 == 2:
        print("\nYour Total Amount Is : ₹",amount)
    elif choice2 == 2 and choice1 == 1:
        print("\nYour Total Amount Is : ₹",total1)
    else:
        print("\nYour Total Amount Is : ₹",amount + amount)
         
         
        
        