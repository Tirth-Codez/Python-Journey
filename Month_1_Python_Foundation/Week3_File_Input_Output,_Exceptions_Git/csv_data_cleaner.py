# 📌 Problem: CSV Data Cleaner
# Given a CSV file with some missing numeric values, the task is to:
# - Read the CSV file.
# - Identify missing values in numeric columns (e.g., Age, Score).
# - Compute the average of each column ignoring blanks.
# - Replace missing values with the computed averages.
# - Save the cleaned data into a new file called cleaned_data.csv.

# 🧠 Approach:
# - Open the CSV file and read the header separately.
# - Read each subsequent line, split by commas, and store as a list of rows.
# - For each numeric column (Age, Score):
#     • Collect non-empty values and convert them to integers.
#     • Compute the average using sum() // len().
# - Loop through all rows:
#     • If a cell is empty, replace it with the column average.
# - Open a new CSV file in write mode.
# - Write the header, then write all cleaned rows back to the file.

f = open("data.csv")
header = f.readline().strip().split(",")
rows = []

for line in f:
    parts = line.strip().split(",")
    rows.append(parts)
    
f.close()
 
age = [int(row[1]) for row in rows if row[1]!=""]
avg_age = sum(age) // len(age)

score = [int(row[2]) for row in rows if row[2]!=""]
avg_score = sum(score) // len(score)

for row in rows:
    if row[1]=="":
        row[1]=str(avg_age)
    if row[2]=="":
        row[2]=str(avg_score)
        
print(rows)

f = open("cleaned_data.csv","w")
f.write(",".join(header) + "\n")
for row in rows:
    f.write(",".join(row) + "\n")

f.close()

