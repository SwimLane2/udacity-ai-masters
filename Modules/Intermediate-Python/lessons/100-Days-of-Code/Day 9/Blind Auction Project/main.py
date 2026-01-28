
import art
print(art.logo)

import os
clear = lambda: os.system('cls')

bid_data = {}
bidder = True
while bidder:
    name = str(input("What is your name?: "))
    price = int(input("What is your bid?: £ "))
    other_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'. "))
    bid_data[name] = price
    if other_bidders == "no":
        bidder = False
        highest_bidder_name = max(bid_data, key=bid_data.get)
        highest_bidder_amount = bid_data[highest_bidder_name]
        print(f"The winner is {highest_bidder_name} with a bid of £{highest_bidder_amount}")
    else:
        clear()

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


