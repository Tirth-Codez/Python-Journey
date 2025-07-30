# 🔄 Problem: Rotate List Left by One Position
# Given a list of elements, rotate the list to the left by one position.
# The first element moves to the end, and all other elements shift one step left.

# 🧠 Approach:
# - Use slicing to split the list:
#     - nums[1:] gets all elements except the first.
#     - nums[:1] gets only the first element as a sublist.
# - Concatenate both slices: the tail followed by the head.
# - This forms the rotated list without using loops or pop/append.

nums=[1,2,3,4]
rotated = nums[1:]+nums[:1]
print(rotated)