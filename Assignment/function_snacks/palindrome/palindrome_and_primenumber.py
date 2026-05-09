def is_prime(number):

    if number < 2:
        return False

    for count in range(2, int(number ** 0.5) + 1):
        if number % count == 0:
            return False

    return True


def is_palindrome(number):

    original = str(number)

    reversed_number = ""

    for character in original:
        reversed_number = character + reversed_number

    if original == reversed_number:
        return True
    else:
        return False

def palindrome_prime(number):

    return is_prime(number) and is_palindrome(number)
