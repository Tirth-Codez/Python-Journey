# 📌 Problem: Count Vowels in a String
# Given a string, count the total number of vowels (a, e, i, o, u) present.
# The check should be case-insensitive.

# 🧠 Approach:
# - Define a tuple or set of vowels.
# - Initialize a counter variable.
# - Loop through each character in the string.
# - Convert the character to lowercase and check if it’s a vowel.
# - If yes, increment the counter.
# - Return or print the final count.

strs = "abcdefghuic"
strs = strs.lower()
vowels = ("a","e","i","o","u")
vowel_count=0
for i in strs:
    if i in vowels:
        vowel_count+=1
print(vowel_count)