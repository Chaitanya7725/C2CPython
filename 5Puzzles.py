import random

# random_float = random.random()
# print(random_float)
# print(f"{random_float:.5f}")

# possible_options =  ['water','pool','cool','air']
# for i in possible_options:
#     print(i)

# print('End')

import random

# List of (question, answer) pairs
questions = [
    ("What is 10 + 10?", "20"),
    ("What is the capital of Texas?", "Austin"),
    ("What was the 9th  planet in our solar system?", "Pluto")
]

score = 0

# Shuffle the questions to ensure random order and no repeats
random.shuffle(questions)

for question, answer in questions:
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")

print(f"Game Over! Your final score is: {score}/{len(questions)}")