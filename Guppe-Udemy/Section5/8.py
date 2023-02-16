num1 = float(input("Enter the first grade: "))
num2 = float(input("Enter the second grade: "))

if (0.0 <= num1 <= 10.0) and (0.0 <= num2 <= 10.0):
    print(f"Average = {(num1+num2)/2}")
else:
    print("You entered a invalid grade value, try again.")
