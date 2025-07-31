# Problem: Remove Duplicates from a List
# Given a list with duplicate elements, return a list containing only the unique elements.

# 🧠 Approach:
# - Convert the list into a set using `set()` to automatically remove duplicates.
# - Convert the set back to a list using `list()`, since sets are unordered collections.
# - Print or return the unique list.

list1 = [1,2,2,3,4,5,6,6]
set1 = set(list1)
list1 = list(set1)
print(list1)