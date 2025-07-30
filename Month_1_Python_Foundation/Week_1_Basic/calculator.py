# 🧮 Menu-Driven Calculator with GCD
# 🧠 Approach:
# - Use a `while True` loop to keep the calculator running until user exits.
# - Take two integer inputs from the user.
# - Show a menu of operations using a multi-line string.
# - Ask the user to choose an operation (1–7).
# - Use if-elif conditions to perform:
#     - 1: Addition → print num1 + num2
#     - 2: Subtraction → print num1 - num2
#     - 3: Multiplication → print num1 * num2
#     - 4: Division → check for division by zero
#     - 5: Power → print num1 raised to num2
#     - 6: GCD → use recursion to calculate GCD (Euclidean algorithm)
#     - 7: Exit the loop and print thank you message
# - If the user enters an invalid choice, print an error message.

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print('''
    Enter 1 for addition
    Enter 2 for subtraction
    Enter 3 for multiplication
    Enter 4 for division
    Enter 5 for power
    Enter 6 for GCD
    Enter 7 to exit
    ''')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Division by zero not possible")
        else:
            print(num1 / num2)
    elif choice == 5:
        print(num1 ** num2)
    elif choice == 6:
        def gcd(num1, num2):
            if num2 == 0:
                print(num1)
            else:
                gcd(num2, num1 % num2)
        gcd(num1, num2)
    elif choice == 7:
        print("Thanks for using the code")
        break
    else:
        print("Invalid choice")
