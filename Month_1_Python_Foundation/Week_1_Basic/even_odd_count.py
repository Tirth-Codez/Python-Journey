# 🔢 Count Even and Odd Numbers
# 💡 Approach:
# - Loop through the list.
# - Use `num % 2 == 0` to check for even.
# - Use counters to keep track of even and odd numbers.

numbers = [11, 8, 5, 2, 17, 20]
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)