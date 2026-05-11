number = int(input("Enter a number: "))

count = 0

for index in range(1, number + 1):
    if number % index == 0:
        count += 1

print("Number of divisors:", count)