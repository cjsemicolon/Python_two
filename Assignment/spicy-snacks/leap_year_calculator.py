# PSEUDOCODE
# Start
# Input year
# If year is divisible by 400
#     Display leap year
# Else if year is divisible by 4
#     and not divisible by 100
#     Display leap year
# Else
#     Display not leap year
# End

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")

elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")

else:
    print(year, "is NOT a Leap Year")
