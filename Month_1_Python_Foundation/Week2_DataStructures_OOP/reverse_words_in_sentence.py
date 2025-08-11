# 📌 Problem: Reverse Words in a Sentence
# Given a sentence, reverse the order of the words while keeping each word's letters in the same order.
# Example:
#   Input:  "The sky is blue"
#   Output: "blue is sky The"

# 🧠 Approach:
# - Use split() to split the sentence into a list of words (automatically removes extra spaces).
# - Reverse the list using slicing [::-1].
# - Use " ".join() to join the reversed list back into a single string with spaces between words.

s = "The sky is blue"
list1 = s.split()
list1 = list1[::-1]
s = " ".join(list1)
print(s)