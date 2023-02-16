grades = []
sum = 0
i = 0
lenght = int(input("How many grades you want to calc?\n"))

while i < lenght:
    grades.append(float(input("Enter a grade between 0.0 and 10.0: ")))
    if grades[i] < 0.0 or grades[i] > 10.0:
        print("You entered a invalid grade value, try again.")
        break
    else:
        sum += grades[i]
        i += 1
if i == lenght:
    print(f"Average = {sum/2}")
else:
    print("Program finished!")

"""
Initialize var i = 0;
Create a loop while counter < lenght(amount of grades)
Append input[i] on grades array
Verifies if [i] grade is valid (between 0.0 and 10.0)
    if is not -> break the loop
    else -> Add the value on var sum and increment the counter i
if counter(i) equals input lenght, it means that all entered grades were valid, so i = lenght
    print Average
else, it means that the entered grade was invalid and, at some point, the loop was broken and counter equals 0, 1 or 2
    end program
"""
