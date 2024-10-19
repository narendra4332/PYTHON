# addition is starting from hear
def addition():
    continuecal = "y"
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 + num_2
    values_entered = 2
    print(f'Current result: {ans}')
    while continuecal == "y":
        continuecal = (input('Enter more (y/n): '))
        while continuecal not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continuecal = (input('Enter more (y/n): '))
        
        if continuecal == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        values_entered+=1
        print(f'Current result: {ans}')
    return[ans,values_entered]


# Subtraction is starting  from hear
def subtraction():
    continuecal = "y"
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 - num_2
    values_entered = 2
    print(f'Current result: {ans}')
    while continuecal == "y":
        continuecal = (input('Enter more (y/n): '))
        while continuecal not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continuecal = (input('Enter more (y/n): '))
        
        if continuecal == 'n':
            break
        num = float(input('Enter another number: '))
        ans -= num
        values_entered+=1
        print(f'Current result: {ans}')
    return[ans,values_entered]

# Multiplication is Starting Start From Here
def multiplication():
    continuecal = "y"
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 * num_2
    values_entered = 2
    print(f'Current result: {ans}')
    while continuecal == "y":
        continuecal = (input('Enter more (y/n): '))
        while continuecal not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continuecal = (input('Enter more (y/n): '))
        
        if continuecal == 'n':
            break
        num = float(input('Enter another number: '))
        ans *= num
        values_entered+=1
        print(f'Current result: {ans}')
    return[ans,values_entered]

# Division is starting from hear
def division():
    continuecal = "y"
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 / num_2
    values_entered = 2
    print(f'Current result: {ans}')
    while continuecal == "y":
        continuecal = (input('Enter more (y/n): '))
        while continuecal not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continuecal = (input('Enter more (y/n): '))
        
        if continuecal == 'n':
            break
        num = float(input('Enter another number: '))
        ans /= num
        values_entered+=1
        print(f'Current result: {ans}')
    return[ans,values_entered]

def calculator():
   quit = False
   while not quit:
       print('Simple Calculator in Python!')
       print('Enter \'a\' for addition')
       print('Enter \'s\' for substraction')
       print('Enter \'m\' for multiplication')
       print('Enter \'d\' for division')
       print('Enter \'q\' to quit',"\n")

       choice = input('Selection: ')

       if choice == 'q':
           quit = True
           continue

       if choice == 'a':
           results = addition()
           print('Ans = ',results[0], 'total inputs :',results[1],"\n")
       elif choice == 's':
           results = subtraction()
           print('Ans = ', results[0], ' total inputs: ', results[1],"\n")
       elif choice == 'm':
           results = multiplication()
           print('Ans = ', results[0], ' total inputs: ', results[1],"\n")
       elif choice == 'd':
           results = division()
           print('Ans = ', results[0], ' total inputs: ', results[1],"\n")
       else:
           print('Sorry, invalid character')
               
calculator()
            

           



