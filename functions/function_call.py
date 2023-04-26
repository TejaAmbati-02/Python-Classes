def teja(**teja):
    for i in teja:
        print(i,end=" ")
    print(teja)
    print(type(teja))
    
teja(name = "teja",age=1,classes = 2,number = 3,rollno = 4,age1 = 5)

def teja1(*teja):
    for i in teja:
        print(i,end=" ")
    print(teja)
    print(type(teja))
    return teja
    
teja1("teja",1,2,3,4,5)


# Call by Reference
a = 10

def validator(a):
    a = a+ 10
    return a
a = validator(a)

print(a)