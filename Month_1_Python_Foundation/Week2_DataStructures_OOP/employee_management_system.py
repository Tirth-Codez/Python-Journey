# 📌 Problem: Company Management System
# Design a system to manage employees in a company using OOP concepts.
# - Create a base class `Employee` with attributes: `name`, `emp_id`, and `salary`.
# - Add methods to:
#     - Display employee details.
#     - Update employee salary.
# - Create subclasses:
#     - `Manager` → has `department` and method `assign_task(employee, task)`.
#     - `Developer` → has `programming_language` and method `complete_task(task)`.
# - Create a `Company` class that maintains a list of employees with methods:
#     - `add_employee(employee)`
#     - `remove_employee(employee)`
#     - `assign_task(manager, employee, task)`
#     - `show_all_employees()`

# 🧠 Approach:
# - Use **inheritance** so `Manager` and `Developer` can reuse attributes/methods from `Employee`.
# - Add extra attributes (`department`, `programming_language`) in subclasses.
# - Implement task assignment by having `Manager.assign_task()` assign tasks to employees,
#   and `Developer.complete_task()` mark them as done.
# - Use a `Company` class with a list to store all employees, and methods to add/remove/manage them.
# - Override `__str__` in `Employee` to print employee details cleanly when listing.

# -----------------------------
# Base Class: Employee
# -----------------------------
class Employee:
    def __init__(self, name, emp_id, salary):
        # Every employee has a name, ID, and salary
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def __str__(self): 
        # String representation of the employee (useful for printing)
        return f"{self.name} (ID: {self.emp_id}, Salary: {self.salary})"

    def display_info(self):
        # Show employee details
        print(f"Name of employee: {self.name}, ID: {self.emp_id}, has salary {self.salary}")

    def update_salary(self, amount):
        # Update employee's salary
        self.salary = amount


# -----------------------------
# Subclass: Manager
# -----------------------------
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        # Initialize Employee attributes + department
        super().__init__(name, emp_id, salary)
        self.department = department

    def assign_task(self, employee, task):
        # Manager assigns a task to an employee
        print(f"{employee.name} has been assigned with task '{task}' by Manager {self.name}")


# -----------------------------
# Subclass: Developer
# -----------------------------
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        # Initialize Employee attributes + programming language
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def complete_task(self, task):
        # Developer completes a task
        print(f"{self.name} completed the task: {task}")


# -----------------------------
# Class: Company
# -----------------------------
class Company:
    def __init__(self):
        # List to store all employees (Managers + Developers)
        self.employees = []

    def add_employee(self, employee):
        # Add an employee to the company
        self.employees.append(employee)
        print(f"{employee} has joined the company")

    def remove_employee(self, employee):
        # Remove an employee from the company
        self.employees.remove(employee)
        print(f"{employee} has left the company")

    def assign_task(self, manager, employee, task):
        # Ask a manager to assign a task to an employee
        manager.assign_task(employee, task)

    def show_all_employees(self):
        # Display all employees in the company
        print("List of employees:")
        for emp in self.employees:
            print(" -", emp)


# -----------------------------
# Example Usage
# -----------------------------
c1 = Company()  # Create a company object

# Create a Manager and a Developer
m1 = Manager("Aarav", 201, 90000, "IT")
d1 = Developer("Tirth", 123, 56000, "Python")

# Add them to the company
c1.add_employee(m1)
c1.add_employee(d1)

# Show all employees
c1.show_all_employees()

# Assign and complete tasks
c1.assign_task(m1, d1, "Develop new feature")
d1.complete_task("Develop new feature")
