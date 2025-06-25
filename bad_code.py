a= int(input ("enter the number"))
b= int(input ("enter the number"))

print("Choose and Operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")

choice = int(input("Enter your choice"))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)
else:
    print("Invalid input")

x = int(input("more? 1 = yes: "))
if x == 1:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Choose operation: 1 = add, 2 = subtract, 3 = multiply, 4 = divide")
    c = int(input())
    if c == 1:
        print("Result is", a + b)
    elif c == 2:
        print("Result is", a - b)
    elif c == 3:
        print("Result is", a * b)
    elif c == 4:
        if b == 0:
            print("can't divide")
        else:
            print("Result is", a / b)
    else:
        print("bad input")

x = int(input("more? 1 = yes: "))
if x == 1:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Choose operation: 1 = add, 2 = subtract, 3 = multiply, 4 = divide")
    c = int(input())
    if c == 1:
        print("Result is", a + b)
    elif c == 2:
        print("Result is", a - b)
    elif c == 3:
        print("Result is", a * b)
    elif c == 4:
        if b == 0:
            print("can't divide")
        else:
            print("Result is", a / b)
    else:
        print("bad input")