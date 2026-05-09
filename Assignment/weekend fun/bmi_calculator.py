# PSEUDOCODE
# Start
# Input weight
# Input height
# Calculate bmi = weight / (height * height)
# Print bmi
# If bmi is less than 18.5
#     Print Underweight
# Else if bmi is between 18.5 and 24.9
#     Print Normal
# Else if bmi is between 25 and 29.9
#     Print Overweight
# Else
#     Print Obese
# End

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")

elif bmi <= 24.9:
    print("Normal")

elif bmi <= 29.9:
    print("Overweight")

else:
    print("Obese")


