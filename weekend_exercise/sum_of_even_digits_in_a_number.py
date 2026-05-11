number = int(input("Enter a number: "))

sum_even = 0

while number > 0:
    digit = number % 10

    if digit % 2 == 0:
        sum_even += digit

    number = number // 10

print("Sum of even digits:", sum_even)