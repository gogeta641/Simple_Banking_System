# put your python code here
number1, number2, operation = float(input()), float(input()), input()

if operation == "+":
    product = number1 + number2
elif operation == "-":
    product = number1 - number2
elif operation == "/":
    product = "Division by 0!" if number2 == 0 else number1 / number2
elif operation == "*":
    product = number1 * number2
elif operation == "mod":
    product = "Division by 0!" if number2 == 0 else number1 % number2
elif operation == "pow":
    product = number1 ** number2
elif operation == "div":
    product = "Division by 0!" if number2 == 0 else number1 // number2
else:
    product = "Unsupported"

print(product)