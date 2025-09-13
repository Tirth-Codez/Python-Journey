# 📌 Problem: Implement a Contact Book CLI
# Create a CLI application to manage contacts with the following functionality:
# - Add a new contact (name, phone, email, address).
# - View all contacts.
# - Search a contact by phone number.
# - Update a contact's phone number.
# - Delete a contact by phone number.
# - Exit the program.
#
# 🧠 Approach:
# - Define a `Contact` class with attributes: `name`, `phone`, `email`, `address` and a `__str__` method.
# - Define a `ContactBook` class to manage a list of `Contact` objects.
# - Implement methods:
#   - `add_contact(contact)` → add new contact
#   - `view_contacts()` → display all contacts
#   - `search_contact(num)` → find and print contact by phone
#   - `update_contact(num)` → update phone number of matching contact
#   - `delete_contact(num)` → remove contact by phone number
# - Build a `while True` CLI loop with menu options (1–6) to call these methods.
# - Validate user input and handle invalid options gracefully.

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"{contact} has been added")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print(f"\nTotal contacts: {len(self.contacts)}")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
    
    def search_contact(self, num):
        for contact in self.contacts:
            if contact.phone == num:
                print(contact)
                return
        print("Contact not found")

    def update_contact(self,num):
        for contact in self.contacts:
            if contact.phone == num:
                ask_num = input("Enter new number: ")
                contact.phone = ask_num
                print("Phone number updated successfully")
                return
        print("Contact not found.")
    
    def delete_contact(self, num):
        for contact in self.contacts:
            if contact.phone == num:
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted.")
                return
        print("Contact not found.")

book = ContactBook()    
while True:
    print('''Welcome to Contact Book (CLI)
    Enter 1 to add contacts
    Enter 2 to view Contacts
    Enter 3 to search contact
    Enter 4 to update contact
    Enter 5 to delete contact
    Enter 6 to exit from program''')
    choice = input("Enter your choice: ")
    if not choice.isdigit():
        print("Please enter a number between 1-6")
        continue
    c = int(choice)
    if c==1:
        name = input("Enter name of person: ")
        phone = input("Enter phone number of person: ")
        email = input("Enter email of person: ")  
        address = input("Enter address of person: ")
        c1 = Contact(name,phone,email,address)
        book.add_contact(c1)
    elif c==2:
        book.view_contacts()
    elif c==3:
        number = input("Enter the number to search: ")
        book.search_contact(number)
    elif c==4:
        number = input("Enter the number to update: ")
        book.update_contact(number)
    elif c==5:
        number = input("Enter the number to delete: ")
        book.delete_contact(number)
    elif c==6:
        print("Program successfully ended. Thanks for using CLI")
        break
    else:
        print("invalid choice, please enter valid choice!")