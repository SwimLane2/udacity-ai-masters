# Learning exercise:
# Do not auto-complete full solutions.
# Focus on explanation and hints only.

import art, random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    total = sum(cards)
    return total


is_game_over = True
while is_game_over:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == 'y':
        print(art.logo)
        user_cards = []
        computer_cards = []
               
        #1. Deal both user and computer a starting hand of 2 random card values.
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        #2. Adding the values
        adding_user_cards = calculate_score(user_cards)
        adding_computer_cards = sum(computer_cards)
        comp_first_card = computer_cards[0]

        print(f"Your cards: {user_cards}, current score: {adding_user_cards}")
        print(f"Computer's first card: {comp_first_card}")


        #2. Detect when computer or user has a blackjack. (Ace + 10 value card).


    
    # elif start_game == 'n':
    #     #is_game_over = False
    #     print(f"Your final hand: {user_cards}, final score: {adding_user_cards}")
    #     print(f"Computer's final hand: {computer_cards}, final score: {adding_computer_cards}")
    #     if adding_computer_cards > adding_user_cards:
    #         print("You lose 😤")
    #     elif adding_computer_cards > 21:
    #         print("Opponent went over. You win 😁")
    #     elif adding_user_cards > 
    #     else:
    #         print("You win 😁")
        





