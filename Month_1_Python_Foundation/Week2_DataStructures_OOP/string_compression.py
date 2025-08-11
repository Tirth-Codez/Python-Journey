# 📌 Problem: String Compression
# Given a string, compress it by replacing each group of consecutive identical characters
# with the character followed by the number of occurrences.
# Example:
#   Input:  "aaabbc"
#   Output: "a3b2c1"

# 🧠 Approach:
# - Initialize an empty result string and set count = 1.
# - Loop from the second character to the end:
#     - If current char == previous char, increment count.
#     - Else, append previous char + count to result and reset count = 1.
# - After the loop, append the last char + count to result to handle the final group.

s = "aaabbc"
count = 1
result = ""
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)