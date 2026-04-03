import contact_actions

print("""
1 Add contact
2 View contact
3 Get contact's information
4 Remove contact
5 Edit contact
6 Exit
""")
while True:
    choice = input("\nChoose an option: ")

    if choice == "1":
        print(contact_actions.add_contact())

    elif choice == "2":
        contact_actions.view_contact()

    elif choice == "3":
        print(contact_actions.contact_information())

    elif choice == "4":
        print(contact_actions.remove_contact())

    elif choice == "5":
        print(contact_actions.edit_contact())

    elif choice == "6":
        break

    else:
        print("Choose between 1-6")
