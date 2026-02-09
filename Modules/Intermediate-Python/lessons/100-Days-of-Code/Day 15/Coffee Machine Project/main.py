MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO #1   Prompt user by asking “What would you like? (espresso/latte/cappuccino) - Completed
#TODO #2 Turn off the Coffee Machine by entering “off” to the prompt - Completed
#TODO # 3 Print report - Completed
#TODO #4 Check resources sufficient? - Completed

import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def handle_choice(choice):
    if choice in MENU:
        if is_resource_sufficient(choice):
            print(f"Resources are sufficient for {choice}.")
    elif choice == "off":
        clear_screen()
        return False
    elif choice == "report":
        print_report()
    else:
        print("Invalid choice")
    return True

money = 0
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def is_resource_sufficient(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    for item, required_amount in ingredients.items():
        if resources[item] < required_amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").strip().lower()
    is_on = handle_choice(choice)



