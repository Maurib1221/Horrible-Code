# Good calculator code

# Calculator functions
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x/y

# Input handling functions
def get_numbers():
    """Prompt user for two numbers and return them as integers."""
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return get_numbers()

# Main calculator Loop (User interaction Logic)
def main():
    """Main function to run calculator app with menu-driven options

    Demonstrates clean code, KISS, and separation of concerns by organizing
    user interaction logic ,mapping, and error handling ."""

    # Mapping user input to operations functions and names
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide)
    }

    while True:
        # Display operations choices
        print("\nChoose operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        # Get user choice
        choice = input("Enter choice: ")
        if choice not in operations:
            print("Invalid choice. Try again.")
            continue

        # Get numbers from user
        num1, num2 = get_numbers()

        # Perform operation
        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)

        # Display result
        print(f"{operation_name} result: {result}")

        # Ask user if they want to perform another calculation
        again = input("Perform another calculation? (y/n): ").lower()
        if again != 'y':
            break

# Program entry point
if __name__ == "__main__":
    main()