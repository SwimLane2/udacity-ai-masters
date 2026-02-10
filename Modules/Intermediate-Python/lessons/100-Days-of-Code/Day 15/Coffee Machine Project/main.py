"""
Coffee Machine Project (Day 15)

Flow:
1) Ask user for drink choice or command (report/off)
2) Check resources for selected drink
3) Process inserted coins
4) Validate transaction and return change if needed
5) Deduct ingredients and serve drink

Globals:
- MENU: drink recipes and costs
- resources: current machine ingredients
- money: total profit collected
"""

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

import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

money = 0  # put near your other global data

def print_report():
    """Print current ingredient levels and total money collected."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

def is_resource_sufficient(drink_name):
    """
    Check whether machine has enough ingredients for the selected drink.

    Args:
        drink_name (str): Key from MENU (e.g., 'latte').

    Returns:
        bool: True if all required ingredients are available, else False.
    """
    ingredients = MENU[drink_name]["ingredients"]
    for item, required_amount in ingredients.items():
        if resources[item] < required_amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """
    Ask user for coin counts and return total inserted money.

    Returns:
        float: Total dollar amount inserted by user.
    """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def is_transaction_successful(money_received, drink_cost):
    """
    Validate payment, update profit, and print change/refund message.

    Args:
        money_received (float): Amount user inserted.
        drink_cost (float): Cost of selected drink.

    Returns:
        bool: True if payment is sufficient, else False.
    """
    global money
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change:.2f} dollars in change.")

    money += drink_cost
    return True

def make_coffee(drink_name):
    """
    Deduct ingredients for selected drink and serve it.

    Args:
        drink_name (str): Key from MENU (e.g., 'espresso').
    """
    ingredients = MENU[drink_name]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")


def run_coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").strip().lower()
        if choice in MENU:
            if is_resource_sufficient(choice):
                payment = process_coins()
                if is_transaction_successful(payment, MENU[choice]["cost"]):
                    make_coffee(choice)
        elif choice == "off":
            clear_screen()
            return False
        elif choice == "report":
            print_report()
        else:
            print("Invalid choice")
    

run_coffee_machine()