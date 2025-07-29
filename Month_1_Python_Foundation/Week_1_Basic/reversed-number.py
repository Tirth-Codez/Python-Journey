# 🔄 Reverse a Number
# 💡 Approach:
# - Use a `while` loop to reverse digits of a number.
# - Extract the last digit using `% 10`.
# - Append it to the reversed number using `rev = rev * 10 + digit`.
# - Remove the last digit from the number using `// 10`.

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)