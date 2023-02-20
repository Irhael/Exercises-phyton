def sum_digits(num):
    sum = 0
    while num > 0:
        resto = num % 10
        num = num // 10  # // == integer division
        sum += resto
    return sum


number = int(input("Enter a positive integer: "))

if number > 0:
    ret = sum_digits(number)
    print(f"The sum of the digits o this number is {ret}")
else:
    print("The entered integer is not positive, please enter a positive integer")