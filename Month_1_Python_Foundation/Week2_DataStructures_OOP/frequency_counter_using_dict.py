# 📌 Problem: Count Frequencies of Elements in a List
# Given a list of integers, count how many times each element appears.

# 🧠 Approach:
# - Initialize an empty dictionary.
# - Iterate through each element in the list.
# - If the element is already in the dictionary, increment its count.
# - If not, add it to the dictionary with count = 1.

A=[1, 2, 2, 3, 1, 1]
count = {}
for i in A:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)