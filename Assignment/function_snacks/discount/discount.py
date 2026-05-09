def apply_discount(item_name, original_price, promo_code):
    promo_code = promo_code.upper()

    if original_price < 0:
        raise ValueError("Price cannot be negative")

    if promo_code == "SAVE10":
        discount_price = original_price * 0.90

    elif promo_code == "HALFOFF":
        discount_price = original_price * 0.50

    else:
        discount_price = original_price

    return round(discount_price, 2)
