# PSEUDOCODE
# Start
# Input first score
# Input second score
# Input third score
# Calculate average
# If average is between 90 and 100
#     Display A
# Else if average is between 80 and 89
#     Display B
# Else if average is between 70 and 79
#     Display C
# Else if average is between 60 and 69
#     Display D
# Else
#     Display F
# End

first_score = float(input("Enter first score: "))
second_score = float(input("Enter second score: "))
third_score = float(input("Enter third score: "))

average = (first_score + second_score + third_score) / 3

print("Average =", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")
