from palindrome_and_primenumber import palindrome_prime

number = int(input("Enter a number: "))

if palindrome_prime(number):
    print("The number is both a palindrome and a prime number.")
else:
    print("The number is NOT both a palindrome and a prime number.")
