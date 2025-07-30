# 🔁 Palindrome String Checker
# 💡 Approach:
# - Take input string and convert it to lowercase.
# - Reverse the string using slicing `[::-1]`.
# - Compare original with reversed.
# - If equal, it's a palindrome.

text = input("Enter a string: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
