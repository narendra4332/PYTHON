
# Add a placeholder for the (price) variable:

price = 60
txt = f"The price is {price} dollars"
print(txt)

# .2f means fixed point number with 2 decimals
price = 60
txt = f"The price is {price:.2f} dollars"
print(txt)

# parform a math opration in the placehoder, and return the resut

txt = f"The price is {20*20} dollars"
print(txt)

# we can perform math oprations on variables:

price = 40
tax = 0.20
txt = f"The priceis {price+(price*tax)} dollars"
print(txt)

# we can parform (if...else) statements inside the placeholder:
price = 49
txt = f"it is very {'expensive' if price>50 else'cheap'}"
print(txt)

txt = f"you can {'give bot' if 18<15 else 'not give bot'}"
print(txt)

#use the string methode upper() to convert a value intoupper case letters:
friuit = "banana"
txt = f"I LOVE {friuit.upper()}"
print(txt)

# use a comma as a thousand separator
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = f"We have {49:<8} chickens."
print(txt)

#Use "b" to convert the number into binary format:

txt = f"The binary version of 5 is {5:b}"

print(txt)

#Use "%" to convert the number into a percentage format:

txt = f"You scored {0.25:%}"
print(txt)

#Or, without any decimals:

txt = f"You scored {0.25:.0%}"
print(txt)
