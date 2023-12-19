from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages
from app.AddressBook import AddressBook

@input_error(error_messages["no_command"])
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def address_book_bot():
    contacts = AddressBook()

    print("Welcome to the assistant bot!") # TODO change msg
    while True:
        user_input = input("Enter a command: ") # TODO change msg
        command, *args = parse_input(user_input)
        message = None

        if command in ["close", "exit"]:
            print("Good bye!") # TODO change msg
            break
        elif command == "hello":
            message = "How can I help you?" # TODO change msg
        else:
            message = "Invalid command." # TODO change msg
        
        if bool(message):
            print(message)
