word = input("Enter word to be reversed: ")
reversed_word = ""
for character in word:
    reversed_word = character + reversed_word
print(reversed_word)
