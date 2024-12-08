# Welcome message and name input
def start_game():
    print("Welcome to the Quiz Game!")
    player_name = input("Please enter your name: ")

    print(f"Hello, {player_name}! Let's get started.")
    
    # Updated questions and possible answers (each answer has a number corresponding to it)
    questions = [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
            "correct": "B"
        },
        {
            "question": "What is the largest animal on Earth?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Shark"],
            "correct": "B"
        },
        {
            "question": "In what year did the Titanic sink?",
            "options": ["A. 1901", "B. 1912", "C. 1920", "D. 1898"],
            "correct": "B"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Au", "B. Ag", "C. Fe", "D. Hg"],
            "correct": "A"
        }
    ]
    
    score = 0
    answers = []

    # Ask the questions
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)

        # Get the player's answer
        player_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Store the answer
        answers.append(player_answer)

        # Check if the answer is correct
        if player_answer == q['correct']:
            print(f"Correct, {player_name}!")
            score += 1
        else:
            print(f"Sorry, {player_name}, that's not correct. The correct answer was {q['correct']}.")

    # Final feedback based on performance
    print(f"\nGame over, {player_name}! Your final score is {score} out of {len(questions)}.")

    # Providing a dynamic response based on the player's answers
    if score == len(questions):
        print(f"Excellent work, {player_name}! You got all the questions right!")
    elif score >= len(questions) / 2:
        print(f"Good job, {player_name}! You know your stuff, but there's room for improvement.")
    else:
        print(f"Don't worry, {player_name}, you'll do better next time! Keep studying and try again.")

# Start the game
start_game()