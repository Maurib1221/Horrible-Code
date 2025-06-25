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

# User interface
def get_numbers():
    """Prompt user for two numbers and return them as integers."""
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return get_numbers()

def main():
    """Main function to run calculator app with menu-driven options."""
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide)
    }