import random

# Initialize score
score = 0

# Welcome message
print("WELCOME TO THE NUMBER GUESSING GAME")
ask_name = input("ENTER YOUR NAME: ")
print(f"Hi {ask_name}")

# Ask if they want to play
ask_if_they_want_to_play = input("Do you want to play? Type 'y' or 'n': ")

if ask_if_they_want_to_play.lower() == 'y':
    # Choose difficulty
    level = input("Choose difficulty: easy (1-50), medium (1-100), hard (1-500): ").lower()
    if level == 'easy':
        comp_num = random.randint(1, 50)
    elif level == 'hard':
        comp_num = random.randint(1, 500)
    else:
        comp_num = random.randint(1, 100)

    # Start the guessing game
    attempts = 0
    your_guess = int(input("Enter a random number: "))
    
    while your_guess != comp_num:
        if your_guess > comp_num:
            print("Too high!")
        else:
            print("Too low!")
        
        attempts += 1
        your_guess = int(input("Try again: "))
    
    print(f"Congratulations! You guessed the number {comp_num} correctly!")
    score += 1
    print(f"Your score: {score}")
    
    # Ask if they want to play again
    play_again = input("Want to play again? (y/n): ")
    while play_again.lower() == 'y':
        # Reset game variables
        if level == 'easy':
            comp_num = random.randint(1, 50)
        elif level == 'hard':
            comp_num = random.randint(1, 500)
        else:
            comp_num = random.randint(1, 100)
        
        attempts = 0
        your_guess = int(input("Enter a random number: "))
        
        while your_guess != comp_num:
            if your_guess > comp_num:
                print("Too high!")
            else:
                print("Too low!")
            
            attempts += 1
            your_guess = int(input("Try again: "))
        
        print(f"Congratulations! You guessed the number {comp_num} correctly!")
        score += 1
        print(f"Your score: {score}")
        
        play_again = input("Want to play again? (y/n): ")
    
elif ask_if_they_want_to_play.lower() == 'n':
    print("Thanks for stopping by!")
