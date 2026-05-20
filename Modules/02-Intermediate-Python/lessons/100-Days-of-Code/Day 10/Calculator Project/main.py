import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

mathematical_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def display_operators():
    for key in mathematical_operations:
        print(key)


def calculate():
    print(art.logo)
    calculation_loop = True
    first_number = float(input("What's the first number?: "))
    while calculation_loop:
        display_operators()
        user_operator = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        calculate_results = mathematical_operations[user_operator](n1=first_number, n2=next_number)
        print(f"{first_number} {user_operator} {next_number} = {calculate_results}")
        continue_calculation = input(f"Type 'y' to continue calculating with {calculate_results}, or type 'n' to start a new calculation: ").lower()
        if continue_calculation == "y":
            first_number = calculate_results
        elif continue_calculation == "n":
            calculation_loop = True
            calculate()

calculate()





        # first_number = calculate_results
        # display_operators()
        # user_operator = input("Pick an operation: ")
        # next_number = float(input("What's the next number?: "))
        # calculate_results = mathematical_operations[user_operator](n1=first_number, n2=next_number)
        # print(f"{first_number} {user_operator} {next_number} = {calculate_results}")
        # continue_calculation = input(f"Type 'y' to continue calculating with {calculate_results}, or type 'n' to start a new calculation: ").lower()
#print(mathematical_operations["*"](n1=4, n2=8))

