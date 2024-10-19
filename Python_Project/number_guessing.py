import random
import math

lower = int(input("Enter Lower Bound : "))
upper = int(input("Enter Upper Bound : "))

x = random.randint(lower,upper)
total_chances = math.ceil(math.log(upper - lower+1,2))
print("\n You Have Only ",total_chances,"Chances To Guess The Integer\n")

count = 0
flag = False

while count< total_chances:
    count+=1

    guess = int(input("\nGuess a number : "))

    if x == guess:
        print("Congratulations you did it in",count,"try")
        flag = True
        break
    elif x > guess:
        print("You guessed too small !")
    elif x < guess:
        print("You guessed too high")

if not flag:
    print("\nBetter Luck Next Time !")
