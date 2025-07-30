# 🔄 Problem: Unpack and Print Elements of Tuple Pairs
# Given a list of 2-element tuples, unpack each tuple inside a loop
# and print both elements in a readable format.

# 🧠 Approach:
# - Use a `for` loop to iterate through the list of tuples.
# - Unpack each tuple directly inside the loop header using `for a, b in list:`.
# - Print both unpacked values with custom labels for clarity.

tp = [(1,2),(3,4),(5,6)]
for a,b in tp:
    print("First:",a," Second:",b)
    