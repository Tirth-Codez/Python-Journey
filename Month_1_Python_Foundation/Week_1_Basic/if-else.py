age = int(input("Enter your age: "))
if age >= 18:
    print("You're eligible to vote.")
elif age > 0:
    print("You're not eligible to vote yet.")
else:
    print("Invalid age.")
