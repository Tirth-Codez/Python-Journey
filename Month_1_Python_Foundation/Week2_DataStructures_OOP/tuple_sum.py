# 🔢 Problem: Sum of Tuple Elements
# Given a tuple of integers, calculate and print the total sum of all its elements.

# 🧠 Approach:
# - Initialize a variable (`total` in this case) to store the sum.
# - Loop through the tuple using index-based iteration.
# - In each iteration, add the current element to the total.
# - After the loop, print the total sum.

tp = (1,2,3,4,5,6)
total=0
for i in range(len(tp)):
    total+=tp[i]
print(total)