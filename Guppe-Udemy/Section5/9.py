salary = float(input("Enter salary amount: "))
loan = float(input("Enter requested loan: "))

if loan > (salary*0.2):
    print("Loan not granted.")
else:
    print("Loan granted.")