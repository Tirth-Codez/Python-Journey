# 📌 Problem: Find the First Non-Repeating Character
# Given a string, return the first character that appears only once.
# If all characters repeat, return a message indicating none found.

# 🧠 Approach:
# - Use a dictionary to count the frequency of each character.
# - Loop through the original string.
# - For each character, check if its count is 1.
# - The first such character is the answer.
# - If none found, print a fallback message.

strs = "xxyyyzzd"
dict1 = {}
for i in strs:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for i in strs:
    if dict1[i]==1:
        print(i)
        break
else:
    print("No non repeating character found")