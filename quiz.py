# Welcome message and quiz dictionary
print("WELCOME TO THE QUIZ GAME")
quiz = {
    "What is the capital of Nepal": {
        "options": ["A. Berlin", "B. Madrid", "C. Pokhara", "D. Kathmandu"],
        "answer": "D"
    },
    "The study of plants is called": {
        "options": ["A. Zoology", "B. Botany", "C. Astronomy", "D. Psychology"],
        "answer": "B"
    },
    "Who painted the Mona Lisa?": {
        "options": ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Claude Monet"],
        "answer": "B"
    },
    "What is the chemical symbol for water?": {
        "options": ["A. CO2", "B. H2O", "C. NaCl", "D. O2"],
        "answer": "B"
    },
    "What year did TikTok launch globally?": {
        "options": ["A. 2016", "B. 2018", "C. 2015", "D. 2020"],
        "answer": "A"
    },
    "Which planet is closest to the sun?": {
        "options": ["A. Venus", "B. Mars", "C. Mercury", "D. Earth"],
        "answer": "C"
    },
    "What does 'www' stand for in a website browser?": {
        "options": ["A. World Wide Web", "B. Web With Widgets", "C. Wireless Web World", "D. Web World Wide"],
        "answer": "A"
    },
    "What does DNA stand for?": {
        "options": ["A. Digital Network Architecture", "B. Deoxyribonucleic Acid", "C. Dynamic Neural Activity", "D. Data Net Array"],
        "answer": "B"
    },
    "Who discovered gravity by watching an apple fall?": {
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo", "D. Stephen Hawking"],
        "answer": "A"
    },
    "Which language is used to style web pages?": {
        "options": ["A. HTML", "B. Python", "C. CSS", "D. Java"],
        "answer": "C"
    }
}

# Ask if the user wants to play
ASK_USER = input("Do you want to play the quiz? Type 'Y' or 'N': ")

# Initialize score
score = 0

# If the user wants to play
if ASK_USER.lower() == 'y':
    # Iterate through each question in the quiz
    for question, q_data in quiz.items():
        print(question)  # Print the question
        
        # Print the options for the current question
        for option in q_data['options']:
            print(option)
        
        # Get the user's answer
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        # Check if the user's answer is correct
        if user_answer == q_data['answer']:
            print("Correct!")
            score += 1  # Increment score
        else:
            print(f"Wrong! The correct answer is {q_data['answer']}.")
    
    # After all questions are asked, display the final score
    print(f"Your final score is: {score}/{len(quiz)}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Y/N): ").lower()
    while play_again == 'y':
        score = 0  # Reset score for the next round
        
        # Repeat the quiz game if user wants to play again
        for question, q_data in quiz.items():
            print(question)
            
            for option in q_data['options']:
                print(option)
            
            user_answer = input("Your answer (A/B/C/D): ").upper()
            
            if user_answer == q_data['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q_data['answer']}.")
        
        print(f"Your final score is: {score}/{len(quiz)}")
        play_again = input("Do you want to play again? (Y/N): ").lower()

    print("Thanks for playing!")
else:
    print("Thanks for stopping by!")
