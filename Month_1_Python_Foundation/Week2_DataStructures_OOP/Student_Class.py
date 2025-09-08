# 📌 Problem: Implement a Student Class
# Given details of a student (name, roll number, and marks), 
# create a class that can store these details and provide methods to:
# - Calculate the student’s average marks.
# - Display the student’s information.

# 🧠 Approach:
# - Define a class `Student` with attributes: `name`, `roll_no`, and `marks`.
# - Implement a method `get_average()` that loops through marks, sums them up,
#   and divides by the number of marks to calculate the average.
# - Implement a method `display_info()` that prints the student’s details
#   in a formatted string.
# - Create an object of the class and call these methods to test functionality. 

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_average(self):
        sum = 0
        for i in self.marks:
            sum+=i
        avg = sum/(len(self.marks))
        print("Average of marks:",avg)
    def display_info(self):
        print(f"Name: {self.name}, Roll no: {self.roll_no}, Marks: {self.marks}")

s1 = Student("Tirth",22,[5,5,5,5,5])
s1.get_average()
s1.display_info()