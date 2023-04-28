n = int(input())


a=0
b=1
print(str(a) + " "+ str(b) + " ")
for i in range(3, n):
        c = a+b
        print(c,end=" ")
        a=b
        b=c