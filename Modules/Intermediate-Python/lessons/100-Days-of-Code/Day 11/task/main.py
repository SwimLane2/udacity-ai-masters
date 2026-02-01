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

def compare_scores(user_score, computer_score):
    """Determine and print the winner based on final scores."""
    # Condition 1: both same score
    if user_score == computer_score:
        print("You both draw 🙈")
    # Condition 2: computer blackjack
    elif computer_score == 0:
        print("You lose 😤")
    # Condition 3: user blackjack
    elif user_score == 0:
        print("You win 😁")
    # Condition 4: user over 21
    elif user_score > 21:
        print("You went over. You lose 😤")
    # Condition 5: computer over 21
    elif computer_score > 21:
        print("Computer went over 21. You win 😁")
    # Condition 6: highest score wins
    else:
        if user_score > computer_score:
            print("You have the highest score. You win 😁")
        else:
            print("Computer has the highest score. You lose 😤")

is_game_over = True
while is_game_over:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == 'y':
        print(art.logo)
        user = []
        computer = []
        #test
               
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
        if user_score == 0 or computer_score == 0 or user_score > 21:
            compare_scores(user_score, computer_score)
        else:
            user_wants_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_wants_card == 'y':
                # deal another card to user
                user.append(deal_card())
                # recalculate user's score
                user_score = calculate_score(user)
                print(f"Your cards: {user}, current score: {user_score}")

                # check if user busted
                if user_score > 21:
                    compare_scores(user_score, computer_score)
                
            # else loop back to ask for another card (nested while loop)
            else:
                # user passes - computer's turn
                # computer must hit until score >= 17
                while computer_score < 17 and computer_score != 0:
                    computer.append(deal_card())
                    computer_score = calculate_score(computer)

                    print(f"Computer's final hand: {computer}, final score: {computer_score}")
                    compare_scores(user_score, computer_score)