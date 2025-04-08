def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. View all the contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    if name in contact_book:
        print("Contact already exists!")
    elif phone in contact_book.values():
        print("Phone number already exists!")
    else:
        contact_book[name] = phone
        print("Contact ",name," added successfully to your Contact Book!")

def view_contacts(contact_book):
    if contact_book:
        print("\nYour Contacts:")
        for name, phone in contact_book.items():
            print("Name: ",name," Phone: ",phone)
    else:
        print("\nNo contacts found!")

def search_contact(contact_book):
    name = input("Enter the name to search: ")
    if name in contact_book:
        print("Contact Found !\nName: ",name," Phone: ",contact_book[name])
    else:
        print("Contact not found in your Contact Book!")

def delete_contact(contact_book):
    name = input("Enter the name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact ",name,"is deleted successfully from your Contact Book!")
    else:
        print("Contact not found in your Contact Book!")

def main():
    contact_book = {}
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contacts(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            print("Exiting the contact book.\nAll Contacts are Deleated from your Contact Book!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()