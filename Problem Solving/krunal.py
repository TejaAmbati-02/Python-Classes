# Kunal is allowed to go out with his friends only on the even days of a given month. Write a program to count the number of days he can go out in the month of August.
# lst = []
# for i in range(1, 32):
#     if(i%2 == 0):
#         lst.append(i)
# even_days = len(lst)
# print(even_days)
# print(31 - even_days)



# lst = []
# for i in range(1,32):
#     if(i%2 != 0):
#         lst.append(i)
# print(len(lst))



# Write a program to print the sum of 
# negative numbers, sum of positive even numbers 
# and the sum of positive odd numbers from a list 
# of numbers (N) entered by the user. The list 
# terminates when the user enters a zero.

lst = [-1,-2,-3,-4,-5,-6,-7,-8,-9,1,2,3,4,5,6,7,8,9]
# print positive numbers

for i in lst:
    if(i > 0):
        print(i)

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15



# (2*3*4) - (2+3+4)

n = 234
mod = 0
mul = 1
while(n > 0):
    a = n//10 
    #  % -> remainder with decimal  // ->  integer division
    mod = mod + a # 4+3
    mul = mul * a # 4*3
    n=n/10 # 234 -> 23 -> 2











