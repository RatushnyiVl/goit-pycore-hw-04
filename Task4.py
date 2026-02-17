def parse_input(user_input:str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args:list, contacts:dict):
    name, phone, *_ = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args:list, contacts:dict):
    name, phone, *_ = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return "No such a name in contacts"

def show_phone(name:str, contacts:dict):
    if name[0] in contacts.keys():
        return contacts.get(name[0])
    else: return "No such a name in contacts"

def show_all(contacts:dict):
    if not contacts:
        return "The list of contacts is empty"
    result = [f'{name}\t{num}' for name, num in contacts.items()]
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input == '':
            continue
        command, *args = parse_input(user_input)

        # not args commands
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == 'all':
            print(show_all(contacts))
            
        # commands with arguments
        elif not args:
            print('Invalid command or no arguments given')
            continue
        elif command == 'add' and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'change' and len(args) == 2:
            print(change_contact(args, contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
