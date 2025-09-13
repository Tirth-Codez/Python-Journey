    for contact in self.contacts:
            if contact.phone == num:
                print(contact)
                return
        print("Contact not found")