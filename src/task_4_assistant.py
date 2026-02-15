def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        print("Invalid command. Usage: add <name> <phone number>")
        return
    name, phone = args
    contacts[name] = phone
    print("Contact added.")

def change_contact(args, contacts):
    if len(args) != 2:
        print("Invalid command. Usage: change <name> <phone number>")
    name, phone = args
    contacts[name] = phone
    print("Contact updated.")

def phone_contact(args, contacts):
    if len(args) != 1:
        print("Invalid command. Usage: phone <name>")
    name = args[0]
    phone = contacts.get(name)
    print(f"Phone number of {name} is {phone}." if phone else f"Contact {name} not found.")

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
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            phone_contact(args, contacts)
        elif command == "all":
            all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()