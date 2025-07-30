# 🔎 Linear Search in List (Without Enumerate)
# 💡 Approach:
# - Take user input for number to search.
# - Loop through list using index (range + len).
# - Compare each element with the target.
# - If found, print index and break.

numbers = [5, 12, 7, 9, 1, 18]
target = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not found in list.")