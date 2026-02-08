import art, game_data, random

def pick_two_entries(data):
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    return a, b

entry_a, entry_b = pick_two_entries(game_data.data)

print(art.logo)
compare_a_text = f"Compare A: {entry_a['name']}, a {entry_a['description']}, from {entry_a['country']}."
print(compare_a_text)

print(art.vs)
compare_b_text = f"Compare B: {entry_b['name']}, a {entry_b['description']}, from {entry_b['country']}."
print(compare_b_text)



# print(input("Who has more followers? Type 'A' or 'B': ").lower())
