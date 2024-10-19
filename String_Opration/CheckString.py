#if we want to check "lodhi" is present in a string, we use the keyword "in"
txt = "hi my name is narendra lodhi"
print("lodhi" in txt)

if "lodhi" in txt:
    print("yes, 'lodhi' is present")

#if we want to check "lodhi" is not present in a string, we use the keyword "NOT in"

print("hello" not in txt)

if "hello" not in txt:
    print("yes, 'hello' not in txt")

print(txt[:5])
print(txt[1:10])
print(txt[0:])
print(txt[-0:])

