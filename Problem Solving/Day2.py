# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# 123
# (1 * 2* 3) - (1+2+3)

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15


n =int(input())
product = 1
sum1 = 0

while(n > 0):
    val = n % 10
    product = product * int(val) # 1 * 4 -> int + float -> float
    sum1 = sum1 + int(val) # 0 + 4
    n = int(n/10)

print("==========")
print(product)
print(sum1)
print(int(product - sum1))


    
