# PSEUDOCODE
# Start
# Input x
# Input y
# If x and y are both zero
#     Print Origin
# Else if y is zero
#     Print X-axis
# Else if x is zero
#     Print Y-axis
# Else if x is positive and y is positive
#     Print Q1
# Else if x is negative and y is positive
#     Print Q2
# Else if x is negative and y is negative
#     Print Q3
# Else
#     Print Q4
# End

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Origin")

elif y == 0:
    print("X-axis")

elif x == 0:
    print("Y-axis")

elif x > 0 and y > 0:
    print("Q1")

elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

else:
    print("Q4")

