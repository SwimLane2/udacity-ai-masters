# Learning exercise:
# Do not auto-complete full solutions.
# Focus on explanation and hints only.

import art, random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(deal_cards):
    total = sum(deal_cards)
    #check for blackjack with two cards only
    if len(deal_cards) == 2 and total == 21:
        return 0  # special blackjack signal

    if 11 in deal_cards and total > 21:
        deal_cards.remove(11)
        deal_cards.append(1)
        total = sum(deal_cards)
    return total

is_game_over = True
while is_game_over:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == 'y':
        print(art.logo)
        user = []
        computer = []
               
        #1. Deal both user and computer a starting hand of 2 random card values.
        for _ in range(2):
            user.append(deal_card())
            computer.append(deal_card())

        #2. Adding the values
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        comp_first_card = computer[0]
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {comp_first_card}")

        #3. Does the user or computer have a blackjack
        if user_score == 0 or computer_score == 0:
            if user_score == 0:
                print("You win 😁")
            elif computer_score:
                print("You lose 😤")
        elif user_score > 21:
            

        



    
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
        





