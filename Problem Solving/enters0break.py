import math
# Take integer inputs till the user enters 0 and print the sum of all numbers


# inputs = int(input("Enter number and 0 to break: "))
# while(inputs != 0):
#     print(inputs)    
#     inputs = int(input("Enter number and 0 to break: "))

sums = 0
while(True):
    inputs = int(input("Enter a value and 0 to exit: "))
    if(inputs == 0):
        break
    sums = sums + inputs
print(sums)