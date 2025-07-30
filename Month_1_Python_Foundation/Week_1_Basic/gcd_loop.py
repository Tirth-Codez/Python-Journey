# 🔁 GCD using Loop
# 💡 Approach:
# - Start with 1, loop till min(num1, num2).
# - Check common divisors using `%`.
# - Update largest common factor.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = 1
for i in range(2, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD is:", gcd)