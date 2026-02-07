import art
from random import *

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = str(input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower())

comp_random_number = randint(1, 100)
print(comp_random_number)


# if difficulty == "easy":
#     print(f"You have 10 attempts remaining to guess the number.")
# else:
#     print(f"You have 5 attempts remaining to guess the number.")