# 🔍 Problem: Find the Second Largest Number in a List
# Given a list of integers, find and print the second largest unique number.
# If no such number exists (e.g., all elements are the same), print a message.

# 🧠 Approach:
# - Initialize two variables: max1 and max2 to negative infinity.
# - Loop through each element in the list:
#     - If the current number is greater than max1:
#         - Set max2 to the previous max1
#         - Update max1 to the current number
#     - Else if the current number is greater than max2 and not equal to max1:
#         - Update max2 to the current number
# - After the loop, check:
#     - If max2 is still negative infinity, it means there was no second largest value


nums = [-1, -2, -4, -6]
max1 = max2 = float('-inf')

for i in range(len(nums)):
    if nums[i] > max1:
        temp = max1
        max1 = nums[i]
        max2 = temp
    elif nums[i] > max2 and nums[i] != max1:
        max2 = nums[i]

if max2 == float('-inf'):
    print("No second largest element exists.")
else:
    print("Second largest:", max2)
