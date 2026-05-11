integer = int(input("Enter a number to be reversed: "))
reversed_number = 0
while integer > 0:
    digit = integer % 10
    reversed_number = reversed_number * 10 + digit
    integer = integer // 10
print(reversed_number)
    
