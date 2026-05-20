
import art
print(art.logo)

import os
clear = lambda: os.system('cls')


def find_highest_bidder(bidding_record):
    highest_bidder_name = max(bidding_record, key=bidding_record.get)
    highest_bidder_amount = bidding_record[highest_bidder_name]
    return print(f"The winner is {highest_bidder_name} with a bid of £{highest_bidder_amount}")

bid_data = {}
bidder = True
while bidder:
    name = str(input("What is your name?: "))
    price = int(input("What is your bid?: £ "))
    other_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'. "))
    bid_data[name] = price
    if other_bidders == "no":
        bidder = False
        find_highest_bidder(bid_data)
    else:
        clear()








# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


