
import art

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

math = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}

print(art.logo)
result = 0.0

while True:

    if result == 0.0:
        number_1 = float(input("What's the first number?"))
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation:")
    number_2 = float(input("What's the next number?"))

    result = math[operation](number_1, number_2)

    print(f"{number_1} {operation} {number_2} = {result}")
    start_new_calculation = input(f"Type 'y' t continue calculating with {result}, or type 'n' to start a new "
                                  f"calculation: ")
    number_1 = result
    if start_new_calculation == "n":
        result = 0.0
        print("\n" * 20)
        print(art.logo)
