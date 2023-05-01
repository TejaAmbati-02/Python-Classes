# voltage 100 -> 5
# 100 to 400 -> 10

voltage = int(input("Enter the voltage consumed: "))


if voltage <= 100:
    print(voltage * 5)
elif voltage > 100 and voltage<400:
    print(voltage * 10)