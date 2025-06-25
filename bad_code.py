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

