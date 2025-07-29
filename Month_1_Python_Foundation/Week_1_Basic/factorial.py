# ✖️ Factorial Using Loop
# 💡 Approach:
# - Take an integer input from the user.
# - Initialize a result variable as 1.
# - Use a `for` loop from 1 to n.
# - Multiply the result with each number in the loop.
# - If input is 0, return 1 by definition.

num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is", fact)
