import art, game_data, random

def pick_two_entries(data):
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    return a, b

def pick_new_b(data, current_a):
    b = random.choice(data)
    while b == current_a:
        b = random.choice(data)
    return b

entry_a, entry_b = pick_two_entries(game_data.data)

last_message = ""
score = 0
result = True
show_final = False
while result:
    # show compare_a_text / compare_b_text
    print(art.logo)
    if last_message:
        print(last_message)

    if show_final:
        break

    compare_a_text = f"Compare A: {entry_a['name']}, a {entry_a['description']}, from {entry_a['country']}."
    print(compare_a_text)

    print(art.vs)
    compare_b_text = f"Compare B: {entry_b['name']}, a {entry_b['description']}, from {entry_b['country']}."
    print(compare_b_text)

    # get user_selection
    user_selection = str(input("Who has more followers? Type 'A' or 'B': ").lower())

    # compute winner
    if entry_a['follower_count'] > entry_b['follower_count']:
        winner = "a"
    else:
        winner = "b"

    if user_selection == winner:
        score += 1
        last_message = f"You're right! Current score: {score}."
        entry_a = entry_b
        entry_b = pick_new_b(game_data.data, entry_a)
    else:
        last_message = f"Sorry, that's wrong. Final score: {score}."
        show_final = True
