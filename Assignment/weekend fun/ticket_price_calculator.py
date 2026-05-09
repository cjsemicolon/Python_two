# PSEUDOCODE
# Start
# Input age
# If age is under 5
#     Print Free
# Else if age is between 5 and 12
#     Print $5
# Else if age is between 13 and 64
#     Print $12
# Else
#     Print $8
# End

age = int(input("Enter age: "))

if age < 5:
    print("Free")

elif age <= 12:
    print("$5")

elif age <= 64:
    print("$12")

else:
    print("$8")
