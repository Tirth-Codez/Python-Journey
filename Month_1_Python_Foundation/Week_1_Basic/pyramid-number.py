# 🔢 Number Pyramid Pattern
# 💡 Approach:
# - Take input for number of rows.
# - Use nested `for` loops:
#     - Outer loop controls the number of rows.
#     - Inner loop prints numbers from 1 to current row index.
# - Print each row on a new line.

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
