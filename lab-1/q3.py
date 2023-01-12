# Write a menu driven program of a calculator - Addition, Subtraction, Multiplication, Division, Modulus

def calculator():
    print("Welcome to the Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    choice = int(input("Enter your choice: "))

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    elif choice == 5:
        print(num1 % num2)
    else:
        print("Invalid choice! Please choose again.")

calculator()