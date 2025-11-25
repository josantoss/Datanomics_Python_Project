# Our quiz is a list of dictionaries (one dictionary = one question)
questions = [
    {
        "question": "What is the capital of Ethiopia?",
        "option1": "Paris",
        "option2": "London",
        "option3": "Addis Ababa",
        "correct": 3
    },
    {
        "question": "What is 2 + 2?",
        "option1": "3",
        "option2": "4",
        "option3": "5",
        "correct": 2
    },
    {
        "question": "What is the largest planet?",
        "option1": "Earth",
        "option2": "Mars",
        "option3": "Jupiter",
        "correct": 3
    },
    {
        "question": "What color is the sky on a clear day?",
        "option1": "Blue",
        "option2": "Green",
        "option3": "Red",
        "correct": 1
    },
    {
        "question": "How many continents are there?",
        "option1": "5",
        "option2": "6",
        "option3": "7",
        "correct": 3
    },
    {
        "question": "What is the currency of the US?",
        "option1": "Yen",
        "option2": "Dollar",
        "option3": "Euro",
        "correct": 2
    }
]
# Counter for correct answers
score = 0
print("=== Welcome to the Quiz! ===\n")
# Loop through each question (6 questions = 0 to 5)
for i in range(6):
    q = questions[i]        # get the dictionary for this question
    print(f"Question {i+1}:")
    print(q["question"])
    print("1.", q["option1"])
    print("2.", q["option2"])
    print("3.", q["option3"])
    # Get answer from user
    answer = input("\nYour answer (1, 2, or 3): ")
    # Check if correct
    if answer == str(q["correct"]):
        print("Correct! Well done!\n")
        score = score + 1
    else:
        print(f"Wrong! The correct answer is {q['correct']}\n")
# Final result
print("=== Quiz Finished! ===")
print(f"Your score: {score} out of 6")
if score == 6:
    print("Perfect score! You're a genius!")
elif score >= 4:
    print("Great job!")
else:
    print("Keep practicing!")