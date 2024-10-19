# simple function

# def simple():
#     print("Hello, My name is narendra lodhi")

# simple()

# Function with argument

# def sumdata(a,b):
#     print(a+b)
    
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# sumdata(num1,num2)

# Fumction with return

# def sumdata(a,b):
#     c = a+b+c
#     return c
# output=sumdata(10,20,10)
# print("sum = ",output)


# Argument

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# def my_function(fname):
#     print(fname+ " Refsnes")
# my_function("narendra")
# my_function("vinay")
# my_function("basant")

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# def  my_function(fname,lname):
#     print(fname+" "+lname)
# my_function("narendra","lodhi")

# def my_function(*kids):
#     print("The youngest child is "+ kids[4])
# my_function("Emil","Tobias","Linus")

# Keyword Argument
# You can also send arguments with the key = value syntax.
# def my_function(child3, child2, child1):
#     print("The youngest child is "+child3)

# my_function(child1 = "Emil", child2="Tobias", child3="linus")


def name(x,y):
    return(f'{x} {y}')
n = name("narendra" , "lodhi")
print(n.upper())