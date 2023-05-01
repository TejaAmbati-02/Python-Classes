# Factorial Program
# 2! = 2*1 = 2
# 5! = 5*4*3*2*1 = 120

number = int(input("Enter a number to find factorial : "))
product = 1
while(number > 0):
    product = product*number
    number = number - 1
print(product)


# number  product
# 5       5 * 1
# 4       5 * 4 *1
# 3       5 * 4 * 3 * 1
# 2       5 * 4 * 3 * 2 *1
# 1       5 * 4 * 3 * 2 * 1 * 1


number = int(input("Enter a number to find factorial : "))
product = 1
for i in range(2, number+1):
    product = product*number
print(product)


