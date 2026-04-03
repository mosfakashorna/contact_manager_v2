import storage


def add_contact():
    name = input("Enter name: ").title()
    phone_number = input("Phone number: ")
    email_address = input("Email address: ").capitalize()
    city = input("City: ").capitalize()

    storage.contacts[name] = {"phone": phone_number,
                              "email": email_address, "city": city}
    storage.save_contact()

    return "\nContact added successfully ✔️"


def view_contact():
    if len(storage.contacts) == 0:
        print("No contacts yet.")

    else:
        print("\nCONTACTS")
        print("--------------------------------------------------------------------------------------------------------")
        print(
            f"{"Serial":<8} | {"Name":<25} | {"Phone Number":<20} | {"Email":<30} | {"City"}")
        print("--------------------------------------------------------------------------------------------------------")

        for i, name in enumerate(storage.contacts, start=1):
            print(
                f"{i:<8} | {name:<25} | {storage.contacts[name]['phone']:<20} | {storage.contacts[name]['email']:<30} | {storage.contacts[name]['city']}")


def contact_information():

    for name in storage.contacts:
        print(name)

    try:
        search_name = input("\nSearch contact name for informations: ").title()

        contact = storage.contacts[search_name]

        output = f"\n{"Name":<7} {search_name}\n"

        for information in contact:
            output += f"{information:<7} {contact[information]}\n"

        return output

    except KeyError:
        return "No contact found."


def remove_contact():
    try:
        print("\nAvailable contacts")
        if len(storage.contacts) == 0:
            print("Empty.")

        else:
            for name in storage.contacts:
                print(name)

            remove_name = input("\nEnter exact name to remove: ").title()

            confirm = input("Are you sure? (y/n): ").lower()

            if confirm == "y":
                storage.contacts.pop(remove_name)
                storage.save_contact()
                return f"\n{remove_name} removed successfully ❌"

            elif confirm == "n":
                return "\nDeletion cancelled."

            else:
                return "\nInvalid choise. Please enter y or n."

    except KeyError:
        return "Contact not found."


def edit_contact():
    if len(storage.contacts) == 0:
        print("Empty.")

    else:
        print("\nAvailable contacts")
        for name in storage.contacts:
            print(name)

        edit_name = input("\nEnter contact name to edit: ").title()

        if edit_name not in storage.contacts:
            print("Contact not found.")

        else:
            contact = storage.contacts[edit_name]

            output = f"\n{"1":<2} {"name":<5} : {edit_name}\n"

            for i, information in enumerate(contact, start=2):
                output += f"{i:<2} {information:<5} : {contact[information]}\n"

            print("\nWhat do you want to edit?")
            print(output)

            choice = input("Choose an option: ")

            if choice == "1":
                old_name = edit_name
                new_name = input("\nEnter new name: ").title()

                if new_name in storage.contacts:
                    return "Contact with this name already exists."

                else:
                    contact_data = storage.contacts[old_name]
                    storage.contacts[new_name] = contact_data

                    storage.contacts.pop(old_name)

            elif choice == "2":
                new_phone = input("\nEnter new phone number: ")
                contact["phone"] = new_phone

            elif choice == "2":
                new_email = input("\nEnter new email: ").title()
                contact["email"] = new_email

            elif choice == "3":
                new_city = input("\nEnter new city: ").title()
                contact["city"] = new_city

            storage.save_contact()
            return "Contact updated successfully."
