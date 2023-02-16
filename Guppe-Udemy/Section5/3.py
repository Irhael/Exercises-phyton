import math

num = float(input("Enter a real number: "))

if num > 0:
    print(math.sqrt(num))
elif num < 0:
    print(num**2)
else:
    print("0")

