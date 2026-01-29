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

print(mathematical_operations["*"](n1=4, n2=8))

