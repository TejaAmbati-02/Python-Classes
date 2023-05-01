# Take integer inputs till the user enters 0 and print the largest number from all.

# previous    inputs
# 0            1           1>0
# 1            2           2>1
# 2            1           1>2
# 2            3           3>2   
# 3

previous = 0
while(True):
    inputs = int(input("Enter a value and 0 to exit: "))
    if(inputs == 0):
        break
    elif inputs > previous:
        previous = inputs
print(previous)
 