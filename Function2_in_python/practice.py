
# If the number of arguments is unknown, add a * before the parameter name:

# Arbitrary Arguments, *args
def my_function(*name):
    print("Your Name Is", name[1])

my_function("narendra", "raja", "abhi")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**name):
    print("Your Name Is", name["first"])

my_function(first = "narendra",second = "raja", third = "abhi")

# Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
my_function(fruits)
