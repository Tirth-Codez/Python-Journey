# 🔍 Find Largest Number in a List
# 💡 Approach:
# - Assume the first element is the max.
# - Loop through list and compare each element.
# - If a larger number is found, update max.

numbers = [10, 4, 23, 87, 2]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value:", maximum)