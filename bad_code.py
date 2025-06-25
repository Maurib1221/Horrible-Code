# BADLY STRUCTURED CALCULATOR

def get_inputs():
    # No input validation, reused badly
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    return a, b

def show_menu():
    # Menu hardcoded, shown multiple times unnecessarily
    print("Choose an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def run_calculator_once():
    a, b = get_inputs()
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid choice")

# Redundant calculator runs without any real loop or reuse
run_calculator_once()
x = int(input("More? 1 = yes: "))
if x == 1:
    run_calculator_once()

x = int(input("More? 1 = yes: "))
if x == 1:
    a, b = get_inputs()
    show_menu()
    c = int(input("Enter your choice: "))
    if c == 1:
        print("Result is", a + b)
    elif c == 2:
        print("Result is", a - b)
    elif c == 3:
        print("Result is", a * b)
    elif c == 4:
        if b == 0:
            print("Can't divide")
        else:
            print("Result is", a / b)
    else:
        print("Bad input")
