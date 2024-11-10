import random

def get_random_integer(min_value, max_value):
    """Generate a random integer within the  given range ."""
    return random.randint(min_value, max_value)

def get_random_operator():
    """Select a random operator: +, -, or *."""
    return random.choice(['+', '-', '*'])

def calculate_problem(num1, num2, operator):
    """Return a math problem as a string and its solution."""
    problem_str = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2
    return problem_str, answer

def math_quiz():
    """Run the Math Quiz game where the user solves random math problems."""
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("Solve the math problems presented.")

    for _ in range(total_questions):
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)
        operator = get_random_operator()

        problem, correct_answer = calculate_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Skip to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
