# contact_manager.py

# Now, I will initialize an empty dictionary to store contacts
contacts = {}

def load_contacts():
    """Load contacts from file"""
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
    except FileNotFoundError:
        pass

def save_contacts():
    """Save contacts to file"""
    with open("contacts.txt", "w") as f:
        for name, contact in contacts.items():
            f.write(f"{name},{contact['phone']},{contact['email']}\n")

def add_contact():
    """Add a new contact"""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        print("Contact added successfully!")

def search_contact():
    """Search for a contact by name"""
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found!")

def update_contact():
    """Update a contact's information"""
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def main():
    load_contacts()
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
