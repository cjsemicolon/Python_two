from arithmatic_app import (
    generate_question,
    ask_question,
    calculate_score
)

total_questions = 10
correct_answers = 0

print("Welcome to the Subtraction Quiz!")

for question in range(1, total_questions + 1):

    print(f"\nQuestion {question}")

    first_number, second_number = generate_question()

    if ask_question(first_number, second_number):
        correct_answers += 1

final_score = calculate_score(
    correct_answers,
    total_questions
)

print("\nQuiz Finished!")
print(f"Correct Answers: {correct_answers}/{total_questions}")
print(f"Final Score: {final_score}%")
