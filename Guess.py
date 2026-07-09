
import random


class Number:
    def __init__ (self, value):
        self.value = value


guess = Number(random.randint(1, 100))

print("Welcome to the Number Guessing Game!")
while True:
    Question= input("Do you want to play the game? (yes/no): ").strip().lower()
    if Question == 'yes':
        while True:
            try:
                user_guess = int(input("Enter your guess (between 1 and 100): "))
                if user_guess < 1 or user_guess > 100:
                    print("Please guess a number within the range of 1 to 100.")
                    continue
                if user_guess < guess.value:
                    print("Too low! Try again.")
                elif user_guess > guess.value:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You've guessed the correct number.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    elif Question == 'no':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")


