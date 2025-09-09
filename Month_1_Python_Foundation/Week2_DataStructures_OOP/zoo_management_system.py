# 📌 Problem: Zoo Management System
# Build a system to represent different animals in a zoo using OOP.
# - Define a base class `Animal` with attributes `name` and `age`.
# - Add methods:
#     - `make_sound()` → prints a generic sound for Animal.
#     - `get_info()` → prints the animal’s name and age.
# - Create derived classes:
#     - `Lion` → overrides `make_sound()` to print "Roar".
#     - `Elephant` → overrides `make_sound()` to print "Trumpet".
#     - `Monkey` → overrides `make_sound()` to print "Chatter".
# - Store different animal classes in a list and iterate to create objects dynamically.
# - Demonstrate polymorphism by calling `make_sound()` for each animal.

# 🧠 Approach:
# - Start with a base class `Animal` having `__init__`, `make_sound()`, and `get_info()`.
# - Use inheritance to define `Lion`, `Elephant`, and `Monkey` classes, each overriding `make_sound()`.
# - Maintain a list of classes `[Lion, Elephant, Monkey]` and loop through it to create instances.
# - Call `make_sound()` on each object to show polymorphism.
# - Also, create an object of `Lion` and call `get_info()` to demonstrate attribute usage.

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Animal makes sound")
    def get_info(self):
        print("Name: ",self.name, " Age: ",self.age)
class Lion(Animal):
    def make_sound(self):
        print("Roar")
class Elephant(Animal):
    def make_sound(self):
        print("Trumpet")
class Monkey(Animal):
    def make_sound(self):
        print("Chatter")

Animals = [Lion,Elephant,Monkey]
for i in Animals:
    p1 = i("Temp",5)
    p1.make_sound()
lion1 = Lion("Simba",6)
lion1.get_info()