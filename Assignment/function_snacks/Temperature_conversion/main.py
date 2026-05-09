from temperature_conversion import temperature_conversion

temp = float(input("Enter temperature: "))
threshold = float(input("Enter threshold: "))
unit = input("Enter unit (C/F): ")

if unit == "":
    result = temperature_conversion(temp, threshold)
else:
    result = temperature_conversion(temp, threshold, unit)

print(result)
