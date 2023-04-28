# Write a program to print whether a number is even or odd, also take
# input from the user.


# input() -> takes string type 
# int() -> converts any type to integer

# number = int(input("Take input "))

# if number%2 == 0:
#     print(f"{number} is even")
#     print(number," is even")
#     print("{} is even".format(number))
# else:
#     print(f"{number} is odd")
#     print(number," is odd")
#     print("{} is odd".format(number))
    
    
# 2. Take name as input and print a greeting message for that particular name.

# name = input("Enter your name please : ")
# print("Hello!! ", name)

# 3. Write a program to input principal, time, and rate (P, T, R) from the user and
# find Simple Interest.

# si = (P*T*R)/100

# principal =  float(input("Enter the principal Amount: "))
# Time =  float(input("Enter the Time : "))
# Rate =  float(input("Enter the Rate: "))

# si = (principal * Time * Rate)/100

# print(si)





# 4. Take in two numbers and an operator (+, -, *, /) and calculate the value.
# (Use if conditions)
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# operator = input("Enter the operator: ")
#  # + - * / % 
# if(operator == '+'):
#     sum = num1 + num2
#     print(sum)
# elif(operator == '-'):
#     sub = num1 - num2
#     print(sub)
# elif(operator == '*'):
#     mul = num1 * num2
#     print(mul)
# elif(operator == '/'):
#     div = num1/num2
#     print(div)
# elif(operator == '%'):
#     mod = num1%num2
#     print(mod)
# else:
#     print("Invalid operator")
# Test case , edge case




# 5. Take 2 numbers as input and print the largest number.
# 6. Input currency in rupees and output in USD.


# 7. To calculate Fibonacci Series up to n numbers.
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...........

        # int a = 0, b = 1;
        # int inputNumber = input.nextInt();

        # System.out.print(a+" "+b+" ");
        # for(int i = 3; i<=inputNumber;i++)
        # {
        #     int c = a+b;
        #     System.out.print(c+" ");
        #     a = b;
        #     b = c;


# a = 0
# b = 1


# 0 1 1 2

# a b    c
# 0 1 -> 1
# 1 1 -> 2
# 1 2 -> 3
# 2 3 -> 5
# 3 5 -> 8


# number = int(input("Enter the number upto how many digits we want : "))
# print(str(a)+" "+ str(b),end=" ")
# for i in range(1, number):
#     c = a + b
#     print(c,end=" ")
#     a = b
#     b = c
    
    

# Fibanocci
# n = int(input())
# a=0
# b=1
# print(str(a) + " "+ str(b),end=" ")
# for i in range(3, n+1):
#         c = a+b
#         print(c,end=" ")
#         a=b
#         b=c
        
# Palindrome
# amma -> amma

# name = input("Enter the string to find palindrome or not: ")

# # for i in range(len(name)-1,0,-1):
# if(name[::-1]==name):
#         print("palindrome")
# else:
#         print("Not")


# 8. To find out whether the given String is Palindrome or not.

# amma  -> amma
# madam -> madam



# Solution 1 
# strings = input("Enter the string to compare for palindrome: ")
# strings1 = ''
# if(strings[::-1] == strings):
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    

# Solution 2
# for i in range(len(strings)-1, 0, -1):
#     if(strings[i] == len(strings)-i+1):
#         print("palindrome")
#     else:
#         print("Not Palindrome")



# 9. To find Armstrong Number between two given number


# 1.6 -> 1 -> .16 -> 1.999999999999999999
# 1.6 -> 2




# 121 -> 3 -> 1**3 + 2***3 + 1**3

# 121 -> len()
# 121%10
# 1&
# 2
# 1

number = int(input("Enter the number to find armstrong number: "))
temp =  number
sum1 = 0

while(number > 0):
        rem = number % 10
        sum1 = (sum1) + rem*rem*rem
        number = number/ 10

if(sum1 == temp):
        print("Yes. It is Armstrong No.")
else:
        print(temp)
        print(sum1)
        print("No. It is not an Armstrong No.")

