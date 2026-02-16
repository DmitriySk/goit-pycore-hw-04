def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

class ContactsManager:
    contacts = {}

    def add(self, args):
        if len(args) != 2:
            return "Invalid command. Usage: add <name> <phone number>"
        name, phone = args
        self.contacts[name] = phone
        return "Contact added."

    def change(self, args):
        if len(args) != 2:
            return "Invalid command. Usage: change <name> <phone number>"
        name, phone = args
        self.contacts[name] = phone
        return "Contact updated."

    def phone(self, args):
        if len(args) != 1:
            return "Invalid command. Usage: phone <name>"
        name = args[0]
        phone = self.contacts.get(name)
        return f"Phone number of {name} is {phone}." if phone else f"Contact {name} not found."

    def all(self):
        if len(self.contacts) == 0:
            return "No contacts in the list."
        return "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())

    def invalid(self):
        return "Invalid command."


def main():
    contacts = ContactsManager()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif hasattr(contacts, command):
            print(getattr(contacts, command)(args))
        else:
            print(contacts.invalid())

if __name__ == "__main__":
    main()