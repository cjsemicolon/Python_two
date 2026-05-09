# PSEUDOCODE
# Start
# Input password
# Find length of password
# If length is less than 1
#     Display invalid
# Else if length is less than 6
#     Display weak
# Else if length is greater than 6
#     and less than or equal to 10
#     Display medium
# Else if length is greater than 10
#     Display strong
# End

password = input("Enter password: ")

length = len(password)

if length < 1:
    print("Password is invalid")

elif length < 6:
    print("Password strength: Weak")

elif length <= 10:
    print("Password strength: Medium")

else:
    print("Password strength: Strong")
