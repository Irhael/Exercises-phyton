import math

num = float(input("Enter a number: "))

if num > 0:
    print(f"The square root of {num} is {math.sqrt((num))}")
    print(f"{num} squared is {num**2}")
elif num < 0:
    print("Invalid number")
else:
    print("0")
