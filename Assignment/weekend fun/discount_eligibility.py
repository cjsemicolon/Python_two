# PSEUDOCODE
# Start
# Input total bill
# Input membership status
# If total bill is greater than or equal to 1000
#     and customer is a member
#         Apply 10% discount
# Else if total bill is greater than or equal to 1000
#     and customer is not a member
#         Apply 5% discount
# Else
#     No discount
# Print discount message
# Print final amount
# End

total_bill = float(input("Enter total bill: "))
is_member = input("Are you a member? (yes/no): ")

if total_bill >= 1000 and is_member == "yes":
    discount = total_bill * 0.10
    final_amount = total_bill - discount

    print("10% discount applied")
    print("Final amount =", final_amount)

elif total_bill >= 1000 and is_member == "no":
    discount = total_bill * 0.05
    final_amount = total_bill - discount

    print("5% discount applied")
    print("Final amount =", final_amount)

else:
    print("No discount")
    print("Final amount =", total_bill)

