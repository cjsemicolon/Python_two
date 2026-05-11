number = input("Enter a number: ")

reversed_number = ""

for character in number:
    reversed_number = character + reversed_number

if number == reversed_number:
    print("Palindrome")
else:
    print("Not palindrome")