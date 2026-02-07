import art
from random import *

def set_attempt(diff):
    if diff == "easy":
        attempt = 10
    else:
        attempt = 5
    return attempt

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = str(input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower())
    target = randint(1, 100)
    attempt = set_attempt(difficulty)

    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == target:
            print(f"You got it! The answer was {target}")
            break
        elif guess > target:
            print(f"Too high.")
            print(f"Guess again")
        elif guess < target:
            print(f"Too less.")
            print(f"Guess again")
        attempt -= 1
    else:
        print(f"You've run out of guesses.")

game()