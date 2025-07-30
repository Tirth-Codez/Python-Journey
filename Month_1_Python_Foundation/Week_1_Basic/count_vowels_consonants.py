# 🔤 Count Vowels and Consonants
# 💡 Approach:
# - Convert string to lowercase.
# - Loop through each character.
# - Use `in` to check if it's a vowel or consonant.
# - Skip non-alphabet characters.

text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)