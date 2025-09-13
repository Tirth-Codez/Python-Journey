# 📌 Problem: Top N Records from CSV by Column
# Given a CSV file with data (first row is header), write a Python program to:
# - Read the CSV file.
# - Sort the rows based on a specific numeric column (here, the 3rd column).
# - Print the top N rows after sorting, along with the header.

# 🧠 Approach:
# - Open the CSV file and read the header separately.
# - Read each subsequent line, split by commas, and store as a list of rows.
# - Convert the target column to integer inside a lambda function to sort numerically.
# - Sort the list of rows in descending order of that column.
# - Print the header.
# - Loop through the first N rows of the sorted list and print them, joining columns with commas.

n = 3
f = open("sample_data.csv")

header = f.readline().strip()
rows = []

for line in f:
    parts = line.strip().split(",") 
    rows.append(parts)

f.close()

rows.sort(key=lambda x: int(x[2]), reverse=True)

print(header)
for i in range(n):
    print(",".join(rows[i]))
