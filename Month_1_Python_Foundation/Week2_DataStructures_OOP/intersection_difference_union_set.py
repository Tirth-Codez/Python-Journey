# 📌 Problem: Perform Basic Set Operations
# Given two sets A and B, find:
# - Elements present in both sets (intersection)
# - Elements present only in A (difference)
# - All unique elements from both sets (union)

# 🧠 Approach:
# - Use `A & B` to get intersection of the sets.
# - Use `A - B` to get difference (elements only in A).
# - Use `A | B` to get union (all unique elements).

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Intersection:",A & B)
print("Difference:", A - B)
print("Union:", A | B)