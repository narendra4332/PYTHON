def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGrater(a,b):
    if(a>b):
        print("First number is grater")
    else:
        print("Second number is grater or equal")

a = 8
b = 10
isGrater(a,b)
calculateGmean(a,b)

c = 10
d = 8
isGrater(c,d)
calculateGmean(c,d)
