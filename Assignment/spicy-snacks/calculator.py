# PSEUDOCODE
# Start
# Input first number
# Input second number
# Input operator
# If operator is +
#     Add numbers
# Else if operator is -
#     Subtract numbers
# Else if operator is *
#     Multiply numbers
# Else if operator is /
#     Divide numbers
# Else
#     Display invalid operator
# End

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print("Result =", first_number + second_number)

elif operator == "-":
    print("Result =", first_number - second_number)

elif operator == "*":
    print("Result =", first_number * second_number)

elif operator == "/":
    print("Result =", first_number / second_number)

else:
    print("Invalid operator")
