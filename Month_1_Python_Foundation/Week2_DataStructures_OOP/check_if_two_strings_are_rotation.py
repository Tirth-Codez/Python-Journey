# 📌 Problem: Check if Two Strings Are Rotations of Each Other
# Given two strings, check whether one string is a rotation of the other.

# 🧠 Approach:
# - Concatenate the first string with itself.
# - If the second string is a substring of this new string, it's a valid rotation.
# - Otherwise, it's not a rotation.

strs = "abcde"
strs1 = "deabc"
strs = strs+strs
if strs1 in strs:
    print("Yes they are rotation")
else:
    print("No they are not rotations")