income = float(input())
tax = 0

if income < 15528:
    tax = 0
elif income < 42708:
    tax = 15
elif income < 132407:
    tax = 25
elif income > 132406:
    tax = 28

calculated_tax = int(round((income * tax / 100), 0))
income = int(income)

print(f"The tax for {income} is {tax}%. That is {calculated_tax} dollars!")