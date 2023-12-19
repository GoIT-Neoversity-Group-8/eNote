from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages, command_messages
from app.AddressBook import AddressBook
from utils.commands import handle_command

@input_error(error_messages["no_command"])
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def address_book_bot():
    contacts = AddressBook()

    print(command_messages["welcome"])
    
    handle_command('help', None, contacts) # TODO if need to show help before start bot, simply remove it
    
    while True:
        user_input = input(command_messages["enter_command"])
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(command_messages["good_bye"]) # TODO change msg
            break
        else:
            handle_command(command, args, contacts)

