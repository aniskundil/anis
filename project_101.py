# import random

# # Define the dictionary of questions and answers
# questions = {
#     "What is the capital of France?": {
#         "A": "Paris",
#         "B": "London",
#         "C": "Berlin",
#         "D": "Rome",
#         "correct": "A"
#     },
#     "Which planet is known as the Red Planet?": {
#         "A": "Mars",
#         "B": "Venus",
#         "C": "Jupiter",
#         "D": "Saturn",
#         "correct": "A"
#     },
#     "What is the chemical symbol for water?": {
#         "A": "H",
#         "B": "O",
#         "C": "HO",
#         "D": "H2O",
#         "correct": "D"
#     },
#     "Who wrote 'To Kill a Mockingbird'?": {
#         "A": "Harper Lee",
#         "B": "Stephen King",
#         "C": "J.K. Rowling",
#         "D": "Charles Dickens",
#         "correct": "A"
#     },
#     "What is the tallest mammal?": {
#         "A": "Elephant",
#         "B": "Giraffe",
#         "C": "Kangaroo",
#         "D": "Horse",
#         "correct": "B"
#     }
# }

# def quiz():
#     score = 0
#     for question, options in questions.items()
#         print(question)
#         for option, answer in options.items():
#             if option != "correct":
#                 print(option + ": " + answer)
        
#       user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
#         if user_answer == options["correct"]:
#             print("Correct!\n")
#             score += 1
#         else:
#             print("Incorrect. The correct answer is", options["correct"] + ".\n")
    
#     print("Your final score is:", score, "out of", len(questions))
#     return score

# def main():
#     play_again = True
#     while play_again:
#         score = quiz()
#         play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"

# if __name__ == "__main__":
#     main()


quiz = [
    {'question': '1. What is the capital of Nigeria?',
     'options': 'a) Kaduna\nb) Lagos\nc) Abuja\nd) Kano\n',
     'answer': 'c'},
    {'question': '2. Which river is the largest in Nigeria?',
     'options': 'a) River Nile\nb) River Kaduna\nc) River Niger\nd) River Kano',
     'answer': 'c'},
    {'question': '3. What is the square root of 81?',
     'options': 'a) 2\nb) 4\nc) 6\nd) 9\n',
     'answer': 'd'}
]
while True:
    score = 0
    for question in quiz:
        print(question['question'])
        print(question['options'])
        user_answer = input("option: ").lower()
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is", question['answer'] ,".\n")
    print(f"Your final score is: {score} out of {len(quiz)}\n")



    replay = input('Would you like to retake the game?: ')
    if replay != 'yes':
        break
print('Thank you for taking the test!')
    
        
