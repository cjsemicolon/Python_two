from discount import apply_discount

item = input("Enter item name: ")
price = float(input("Enter original price: "))
code = input("Enter promo code: ")

final_price = apply_discount(item, price, code)

print("Discounted price:", final_price)
