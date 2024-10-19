employe ={
    'name' :'narendra',
    'id': 123,
    'email':'narendra@gmail.com'
}

# 1. get()
print(employe.get("id"))
# also can get like this:
print(employe["id"],"\n")

# 2. keys()
for element in employe.keys():
    print(element)
print("\n")

# 3. values()
for value in employe.values():
    print(value)
print("\n")

# 4. item()
for a,b in employe.items():
    print(a,b)
print("\n")

# del - with the help of del we can delet data in dictionaries using keys()
# del employe['name']
# print(employe)

# pop() - pop() is also ues for delet data from dictionaries and it returens deleted values.
# employe.pop("name")
# print(employe)

print(employe.pop("name"))
print("\n")

# dict() - it id usedto creat dictionaries

thisdict = dict(name="narendra",branch="cse",)
print(thisdict)
print("\n")

# update() - 
employe.update({'id':'321'})
print(employe)
print("\n")

#clear() - 
employe.clear()
print(employe)
print("\n")

# To insert any key or value
employe['course'] = 'B.Tech'
print(employe)












