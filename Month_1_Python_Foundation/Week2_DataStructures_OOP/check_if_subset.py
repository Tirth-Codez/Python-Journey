# 📌 Problem: Check If a Set is a Subset of Another
# Given two sets A and B, check whether A is a subset of B.

# 🧠 Approach:
# - Use the subset operator `<=` to check if A is a subset of B.
# - If true, print confirmation; otherwise, print that it’s not a subset.

A = {2, 3}
B = {1, 2, 3, 4}
if A<=B:
    print(A," is subset of ",B)
else:
    print(A," is not a subset of ",B)