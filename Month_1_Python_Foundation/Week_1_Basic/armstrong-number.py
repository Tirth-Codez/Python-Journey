# 💥 Armstrong Number Checker
# 💡 Approach:
# - Input a number and store a copy.
# - Use a while loop to get each digit using %10.
# - Cube the digit and add to a total.
# - Check if the total equals the original number.

num = int(input("Enter a number: "))
original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** 3
    num = num // 10

if total == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")
