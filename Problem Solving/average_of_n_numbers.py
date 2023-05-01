# Calculate Average Of N Numbers
import math

number = int(input("Enter a value N : "))

remainder = number
sums = 0
while(number > 0):
    numbers = int(input("Enter number to find average : "))
    sums = numbers+sums
    number = number - 1

print(sums/remainder)






r = int(input("Enter a value N : "))
area = math.pi * r * r
print(area)



# Average of N= sum(N)/N
# number  ->  5
# 1 number -> 5
# 2 number -> 4
# 3 number -> 3
# 4 number -> 2
# 5 number -> 1
# sums = 1 + 2+ 3+ 4+ 5 = 15
# sums/remainder -> 15/5 = 3.0

