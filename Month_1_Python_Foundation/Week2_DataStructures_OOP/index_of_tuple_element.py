# Problem: Find the Index of a Value in a Tuple (Without Using `.index()`)
# Given a tuple and a target value, find and print the index of the first occurrence
# of that value in the tuple. Do not use the built-in `.index()` method.

# 🧠 Approach:
# - Initialize a counter variable (like `i = 0`) to track the index.
# - Loop through the tuple elements one by one.
# - In each iteration, compare the current element with the target value.
# - If a match is found, print the current index and break the loop.
# - If not found after the loop ends, handle the "not found" case if needed.

tp = (1,2,3,4,5,6,7,8)
target = 7
flag=False
for i in range(len(tp)):
    if tp[i]==target:
        print("Element found at index:",i)
        flag = True
        break
if not flag:
    print("Element not found in tuple")