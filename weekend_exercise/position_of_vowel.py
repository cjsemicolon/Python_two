text = input("Enter a string: ")

vowels = "aeiouAEIOU"

for index in range(len(text)):
    if text[index] in vowels:
        print("First vowel position:", index)
        break