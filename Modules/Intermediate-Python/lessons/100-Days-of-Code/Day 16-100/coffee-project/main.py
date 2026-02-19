from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").strip().lower()

    if choice == "off":
        is_on = False
        clear_screen()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(f"{drink}, is being prepared")
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                print(f"{drink.name} costs {drink.cost}")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)