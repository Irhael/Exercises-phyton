gender = input("Enter your gender at birth. Type 'M' for Male and 'F' for Female: ")
aux = gender.upper()
height = float(input("Enter your height: "))
ideal_weight = 0

if aux == 'M':
    ideal_weight = ((72.7 * height) - 58)
    print(f"Your ideal weight is {ideal_weight}kg.")
else:
    ideal_weight = ((62.1 * height) - 44.7)
    print(f"Your ideal weight is {ideal_weight}kg.")