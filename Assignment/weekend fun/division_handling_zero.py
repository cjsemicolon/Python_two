# PSEUDOCODE
# Start
# Input x
# Input y
# If y is not equal to 0
#     Divide x by y
#     Print result
# Else
#     Print cannot divide by zero
# End

x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

if y != 0:
    print("Result =", x / y)
else:
    print("Cannot divide by zero")

