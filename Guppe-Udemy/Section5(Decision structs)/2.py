import math

num = int(input("Enter a number: "))

if num > 0:
    print(math.sqrt(num))
elif num < 0:
    print("Invalid number!")
else:
    print("0")