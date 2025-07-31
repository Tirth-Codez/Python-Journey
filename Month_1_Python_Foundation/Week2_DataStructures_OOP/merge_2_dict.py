# 📌 Problem: Merge Two Dictionaries and Sum Common Keys
# Given two dictionaries, merge them into one. If a key appears in both, sum the values.

# 🧠 Approach:
# - Initialize an empty dictionary.
# - Add all key-value pairs from the first dictionary.
# - Loop through the second dictionary:
#   - If the key exists in the merged dict, add the values together.
#   - Otherwise, simply add the key-value pair to the merged dict.

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {}
for i in d1:
    merged[i] = d1[i]
for i in d2:
    if i in merged:
        merged[i]+=d2[i]
    else:
        merged[i]=d2[i]
print(merged)