# Ask user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, //, **, %): ")

# Perform arithmetic operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
elif operator == '**':
    result = num1 ** num2
elif operator == '//':
    result = num1 // num2
elif operator == '%':
    result = num1 % num2
else:
    print("Invalid operator")
    exit()

# Print result
print(num1, operator, num2, "=", result)
