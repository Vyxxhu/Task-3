import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print(f"Editing contact: {name}")
        phone = input("Enter the new phone number (press enter to keep current): ")
        email = input("Enter the new email address (press enter to keep current): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print("Contact edited successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager Menu:")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
