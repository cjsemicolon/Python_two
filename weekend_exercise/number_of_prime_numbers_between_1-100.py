count = 0

for number in range(2, 101):

    is_prime = True

    for integer in range(2, number):
        if number % integer == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print("Prime numbers count:", count)