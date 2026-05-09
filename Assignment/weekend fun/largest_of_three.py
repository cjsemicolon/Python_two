# PSEUDOCODE
# Start
# Input a
# Input b
# Input c
# Assume a is the largest
# If b is greater than largest
#     Make b the largest
# If c is greater than largest
#     Make c the largest
# Print largest
# End

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest number =", largest)

