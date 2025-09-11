# 📌 Problem: Library Management System
# Build a system to manage books and members in a library using OOP concepts.
# - Create a class `Book` with attributes: `title`, `author`, and `isbn`.
# - Create a class `Member` with attributes: `name`, `member_id`, and a list of `borrowed_books`.
# - Add methods in `Member`:
#     - `borrow_book(book)` → allows borrowing if within the limit.
#     - `return_book(book)` → removes book from borrowed list.
# - Create subclasses `StudentMember` (limit = 3 books) and `TeacherMember` (limit = 5 books).
# - Create a class `Library` with a collection of books and methods:
#     - `add_book(book)`
#     - `remove_book(book)`
#     - `lend_book(member, book)`
#     - `accept_return(member, book)`
# - Ensure borrowing rules are respected (students = 3, teachers = 5).

# 🧠 Approach:
# - Define a `Book` class to represent each book with `title`, `author`, and `isbn`.
# - Define a `Member` base class that tracks borrowed books and has methods
#   for borrowing and returning.
# - Use inheritance to create `StudentMember` and `TeacherMember` classes
#   with different borrowing limits by overriding the `borrow_book` method.
# - Define a `Library` class to store books and handle adding, removing,
#   lending, and accepting returns.
# - Use method calls like `member.borrow_book(book)` and `member.return_book(book)`
#   to enforce borrowing/return rules, while the `Library` manages the central collection.

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:  # default limit
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{self.name} has reached the borrowing limit.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")


class StudentMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:
            super().borrow_book(book)
        else:
            print(f"{self.name} cannot borrow more than 3 books.")


class TeacherMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 5:
            super().borrow_book(book)
        else:
            print(f"{self.name} cannot borrow more than 5 books.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book removed: {book}")

    def lend_book(self, member, book):
        if book in self.books:
            self.books.remove(book)
            member.borrow_book(book)
        else:
            print(f"{book.title} is not available in the library.")

    def accept_return(self, member, book):
        if book in member.borrowed_books:
            member.return_book(book)
            self.books.append(book)

library = Library()
b1 = Book("Python Basics", "Author A", "111")
b2 = Book("AI Fundamentals", "Author B", "222")

library.add_book(b1)
library.add_book(b2)

s1 = StudentMember("Tirth", 101)
t1 = TeacherMember("Prof. Kage", 201)

library.lend_book(s1, b1)
library.lend_book(t1, b2)   

library.accept_return(s1, b1)  
