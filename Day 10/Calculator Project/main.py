def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate(v1=None):
    if v1 is None:
        v1 = float(input("Whats the first number?: "))
    operation = input("+\n-\n*\n/\nPick an Operation: ")
    v2 = float(input("Whats the second number?: "))
    result = float(calculations[operation](v1,v2))
    print(f"{v1} {operation} {v2} = {result}")
    evaluate = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a  new "
                     f"calculation, or type 'end' to end this session: ")
    if evaluate == "y":
        return calculate(result)
    if evaluate == "n":
        print("\n"*20)
        return None
    if evaluate == "end":
        global newcalc
        newcalc = True
        return

newcalc = False

while not newcalc:
    calculate()
