"""Main module"""
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from eNote.constants.messages import command_messages, error_messages
from eNote.app.AddressBook import AddressBook
from eNote.utils.commands import handle_command, command_keys, command_parameters
from eNote.utils.input_handlers import parse_input
from eNote.utils.print_handlers import print_error, print_hint

# Define a custom style with a specific text color
custom_style = Style.from_dict({
    # 'rprompt': 'bg:#00ff00 #000000',
    'prompt': '#00FFFF',  # This sets the text color of the prompt
})

class CommandCompleter(Completer):
    """Class for cli completer implementations."""
    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor

        # Split the input to get the command
        if text_before_cursor:
            command, *rest = text_before_cursor.split()
        else:
            command = ""

        # If there's a command and it is in the list
        if command:
            for cmd in command_keys:
                if cmd.startswith(command) and cmd != command:
                    display_meta = HTML(
                        f'Params: <ansired>{" ".join(command_parameters[cmd])}</ansired>'
                    ) if cmd in command_parameters else 'Command'
                    yield Completion(
                        cmd,
                        start_position=-len(command),
                        display=HTML(f'<ansiblue>{cmd}</ansiblue>: '),
                        display_meta=display_meta
                    )

# Create a PromptSession with the custom completer
session = PromptSession(completer=CommandCompleter())

def address_book_bot():
    """Main function."""
    contacts = AddressBook()

    print_hint(command_messages["welcome"])

    # TODO if no need to show help before start bot, simply remove it
    handle_command('help', None, contacts)

    while True:
        user_input = session.prompt(command_messages["enter_command"], style=custom_style)

        if user_input:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print_hint(command_messages["good_bye"])
                contacts.save_data()
                break
            else:
                handle_command(command, args, contacts)
        else:
            print_error(error_messages["no_command"])
