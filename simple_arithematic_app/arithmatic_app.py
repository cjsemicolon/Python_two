import random


def generate_question():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)

    # Prevent negative answers
    if second_number > first_number:
        first_number, second_number = second_number, first_number

    return first_number, second_number


def check_answer(first_number, second_number, user_answer):
    correct_answer = first_number - second_number
    return user_answer == correct_answer


def ask_question(first_number, second_number):
    attempts = 2

    while attempts > 0:
        answer = int(input(f"What is {first_number} - {second_number}? "))

        if check_answer(first_number, second_number, answer):
            print("Correct!")
            return True

        attempts -= 1

        if attempts > 0:
            print("Wrong answer. Try again.")

    print("Incorrect.")
    return False


def calculate_score(correct_answers, total_questions):
    return (correct_answers / total_questions) * 100
