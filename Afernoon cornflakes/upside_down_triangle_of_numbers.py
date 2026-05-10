user_choice = int(input("Enter a  number"))
for number in range(user_choice, 0, -1):
    for count in range(number, 0, -1):
        print(count, end=" ")
    print()
