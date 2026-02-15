def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} changed to {phone}."

def phone_contact(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    return f"Phone number of {name} is {phone}." if phone else f"Contact {name} not found."

def all_contacts(contacts):
    for contact in contacts.items():
        name, phone = contact
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
            print("Contact added.")
        elif command == "change":
            change_contact(args, contacts)
            print("Contact updated.")
        elif command == "phone":
            phone = phone_contact(args, contacts)
            print(phone)
        elif command == "all":
            all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()