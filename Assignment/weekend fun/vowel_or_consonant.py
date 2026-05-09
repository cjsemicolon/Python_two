# PSEUDOCODE
# Start
# Input a letter
# Convert letter to lowercase
# If input is not alphabetic
#     Print Invalid input
# Else if letter is a vowel
#     Print Vowel
# Else
#     Print Consonant
# End

letter = input("Enter a letter: ")

letter = letter.lower()

if letter.isalpha() == False or len(letter) != 1:
    print("Invalid input")

elif letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")

else:
    print("Consonant")
