# 📌 Problem: Invert a Dictionary
# Given a dictionary with unique values, create a new dictionary that flips keys and values.

# 🧠 Approach:
# - Initialize an empty dictionary.
# - Loop through each key in the original dictionary.
# - In the new dictionary, set the value as the key and the key as the value.

d = {'a': 1, 'b': 2, 'c': 3}
new_d = {}
for x in d.keys():
    new_d[d[x]]=x
print(new_d)