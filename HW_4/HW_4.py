# Парсинг вводу користувача
def parse_input(user_input):

    # Перевірка на порожній ввід
    if not user_input.strip(): 
        return ("",)
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


# додавання нового контакту
def add_contact(args, contacts):

    if len(args) != 2:
        return "Invalid command."
    
    name, phone = args
    name = name.lower()
    contacts[name] = phone

    return "Contact added."


# зміна номера телефону існуючого контакту
def change_contact(args, contacts):

    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    name = name.lower()

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    
    else:
        return "Contact not found."


# відображення номера телефону контакту 
def show_phone(args, contacts):

    if len(args) != 1:
        return "Invalid command."
    
    name = args[0]
    name = name.lower()

    if name in contacts:
        phone = contacts[name]
        return phone
    else:
        return "Contact not found."


# відображення всіх контактів
def show_all(contacts):

    if contacts:
        result = []

        for name, phone in contacts.items():
            name = name.capitalize()
            result.append(f"{name}: {phone}")

        return "\n".join(result)
    
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)    

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
