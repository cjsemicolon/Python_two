# PSEUDOCODE
# Start
# Input father's age
# Input son's age
# Calculate difference using years = absolute value of (father_age - 2 * son_age)
# Display result
# End

father_age = int(input("Enter father's age: "))
son_age = int(input("Enter son's age: "))

years = abs(father_age - (2 * son_age))

print(years)
