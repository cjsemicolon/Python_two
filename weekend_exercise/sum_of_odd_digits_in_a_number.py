number = int(input("Enter a number: "))

sum_odd = 0

while number > 0:
    digit = number % 10

    if digit % 2 != 0:
        sum_odd += digit

    number = number // 10

print("Sum of odd digits:", sum_odd)