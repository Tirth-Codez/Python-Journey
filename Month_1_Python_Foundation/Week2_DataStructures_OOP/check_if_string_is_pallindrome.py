# 📌 Problem: Check if a String is a Palindrome
# Given a string, check whether it is a palindrome.
# A palindrome reads the same forward and backward. Ignore case sensitivity.

# 🧠 Approach:
# - Convert the string to lowercase.
# - Reverse the string using slicing (`[::-1]`).
# - Compare the original (lowercased) string with the reversed version.
# - If both match, it's a palindrome. Otherwise, it is not.

strs = "abcdefghi"
strs1 = "ABBA"
strs = strs.lower()
strs1 = strs1.lower()
if strs==strs[::-1]:
    print("First string is pallindrome")
else:
    print("First string is not pallindrome")

if strs1==strs1[::-1]:
    print("Second string is pallindrome")
else:
    print("Second string is not pallindrome")