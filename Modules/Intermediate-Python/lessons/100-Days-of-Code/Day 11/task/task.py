import random

def deal_card():
    #Returns a random card from the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    #Take a list of cards and return the score calculated from the cards
    total = sum(cards)
    #check for blackjack with two cards only
    if len(cards) == 2 and total == 21:
        return 0  # special blackjack signal

    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)
    return total

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
