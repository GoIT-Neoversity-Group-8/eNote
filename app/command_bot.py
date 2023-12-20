from constants.messages import command_messages, error_messages
from app.AddressBook import AddressBook
from utils.commands import handle_command, command_keys, command_parameters
from utils.input_handlers import parse_input
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML

class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor

        # Split the input to get the command
        command, *rest = text_before_cursor.split()

        # If there's a command and it is in the list
        if command:            
            for cmd in command_keys:
                if cmd.startswith(command) and cmd != command:
                    display_meta = HTML(f'Params: <ansired>{" ".join(command_parameters[cmd])}</ansired>') if cmd in command_parameters else 'Command'
                    yield Completion(cmd, start_position=-len(command), display=HTML(f'<ansiblue>{cmd}</ansiblue>: '), display_meta=display_meta)

# Create a PromptSession with the custom completer
session = PromptSession(completer=CommandCompleter())

def address_book_bot():
    contacts = AddressBook()

    print(command_messages["welcome"])
    
    handle_command('help', None, contacts) # TODO if no need to show help before start bot, simply remove it
    
    while True:
        user_input = session.prompt(command_messages["enter_command"])

        if user_input:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(command_messages["good_bye"])
                break
            else:
                handle_command(command, args, contacts)
        else:
            print(error_messages["no_command"])

