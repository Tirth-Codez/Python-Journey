# 📌 Problem: Check if Two Strings are Anagrams
# Given two strings, determine if they are anagrams of each other.
# An anagram contains the same characters with the same frequencies, regardless of order or case.

# 🧠 Approach:
# - Convert both strings to lowercase to ensure case-insensitive comparison.
# - Create two dictionaries to store the frequency of each character in both strings.
# - Loop through each character in both strings and update their respective counts.
# - Finally, compare the two dictionaries:
#     - If they are equal, the strings are anagrams.
#     - Otherwise, they are not.

strs1 = "listen"
strs2 = "silent"
strs1 = strs1.lower()
strs2 = strs2.lower()
dict1 = {}
dict2 = {}
for i in strs1:
    if i in dict1.keys():
        dict1[i]+=1
    else:
        dict1[i]=1
for i in strs2:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
if dict1==dict2:
    print("Strings are anagram")
else:
    print("Strings are not anagram")