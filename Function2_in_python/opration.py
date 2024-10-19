import math
flag = True
while flag:
    number = int(input('''
            1 For Addition
            2 For Subtraction
            3 For Multiplication
            4 For Division
            5 For Modulus
            6 For Check Even & odd
            7 For Factorial
            8 For Check Square Root
            9 For Check Leap Year
            10 For Check Armstorng Number
            11 For Convert KM To Miles
            12 For Covert Celsius To Fahrenheit
            13 For Check Prime Number
            14 for Break !
                       
            Enter Your Choise : '''))
    def Add(num1,num2):
        print("Addition = ",num1+num2)

    def Sub(num1,num2):
        print("Subtraction = ",num1-num2)

    def Mul(num1,num2):
        print("Multiplication =",num1*num2)

    def Div(num1,num2):
        print("Division = ",num1/num2)

    def Mod(num1,num2):
        print("Modulus = ",num1%num2)

    def Even_odd():
        a = int(input("Enter any number :"))
        if a%2==0:
            print(a,"is even number")
        else:
            print(a,"is odd number")

    def Factorial():
        b = int(input("Enter any number :"))
        fact = 1
        if b < 0:
            print("factorial of 0 does not exist")
        elif b == 0:
            print("factorial of 0 is",1)
        elif b > 0:
            for element in range(1,b+1):
                fact = fact*element
        print(f'factorial of {element} is {fact}')
    
    def sqr():
        c = int(input("Enter number : "))
        sr = math.sqrt(c)
        print("square root of ",c,"is :",sr)

    def LeapYear():
        year = int(input("Enter a year : "))
        if year%400==0 and year%100==0:
            print(year,"is leap year")
        elif year%4==0 and year%100!=0:
            print(year,"is leap year")
        else:
            print(year,"is not leap year")
    
    def Armstrong():
        arm = int(input("Enter any number :"))
        sum = 0
        temp = arm
        while temp>0:
            digit = temp%10
            cube = digit**3
            sum = sum+cube
            temp //=10

        if sum == arm:
            print(arm,"is a armstong number")
        else:
            print(arm,"is not a armstong number")

    def km_miles():
        km = int(input("Enter km hear: "))
        miles = km*(0.621731)
        print(f'{km} kms will be {miles} miles')

    def Celsius_Fahrenheit():
        celsius = int(input("Enter Temperature in celsius :"))
        fahrenheit = (celsius*1.8)+32
        print("fahrenheit is = ",fahrenheit)

    def CheckPrime():
        prime = int(input("Plese enter number: "))
        if prime == 1:
            print(prime, "is not a prime number")
        elif prime > 1:
            for element in range(2,prime):
                if prime%element == 0:
                    print(prime,"is not a prime number")
                    break
            else:
                print(prime,"is a prime number")

    if number == 6:
        Even_odd()
    elif number == 7:
        Factorial()
    elif number == 8:
        sqr()
    elif number == 9:
        LeapYear()
    elif number == 10:
        Armstrong()
    elif number == 11:
        km_miles()
    elif number == 12:
        Celsius_Fahrenheit()
    elif number == 13:
        CheckPrime()
    elif number == 14:
        break
        

    if number!=6 and number!=7 and number!=8 and number!=9 and number!=10 and number!=11 and number!=12 and number!=13:
        try:
            num1 = int(input("\nEnter First Number: "))
            num2 = int(input("Enter Second Number: "))
        except:
            print("WORANG INPUT !")
        else:
            if number == 1:
                Add(num1,num2)
            elif number == 2:
                Sub(num1,num2)
            elif number == 3:
                Mul(num1,num2)
            elif number == 4:
                Div(num1,num2)
            elif number == 5:
                Mod(num1,num2)


