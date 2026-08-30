contacts = {}  # key: name, value: dict with phone and email


def add_contact():
    """Add a new contact."""
    name = input("Enter name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists. Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")


def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"Contact '{name}' not found.")


def update_contact():
    """Update an existing contact's details."""
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return

    print("Leave a field blank to keep it unchanged.")
    phone = input(f"Enter new phone (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    print(f"Contact '{name}' updated successfully.")


def delete_contact():
    """Delete a contact by name."""
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")


def list_contacts():
    """Display all contacts."""
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n--- All Contacts ---")
    for name, details in contacts.items():
        print(f"{name}: {details['phone']} | {details['email']}")


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")


def main():
    print("=== Welcome to the Contact Book ===")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()