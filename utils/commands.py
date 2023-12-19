from app.command_handlers import *

def bot_help(args, book):
    print("\nAvailable commands:")
    print("|{:_^15}|{:_^45}|{:_^60}|".format("Command", "Example with arguments", "Description"))
    for command, info in command_info.items():
        description = info['description']
        example = info['example']
        print("|{:<15}|{:<45}|{:<60}|".format(command, (' ' if example is None else f'example: {example}'), description))
    print("\n")

command_info = {
    'help': {
        'function': bot_help,
        'example': None,
        'description': 'Shows a list of available commands with descriptions.',
    },
    'hello': {
        'function': bot_hello,
        'example': None,
        'description': 'Greets the user.',
    },
    'exit, close': {
        'function': None,  # No function associated with exit, it will be handled separately
        'example': None,
        'description': 'Exits the program.',
    },
    'all': {
        'function': show_all,
        'example': None,
        'description': 'Show all contacts, ordered by name',
    },
    'add-contact': {
        'function': add_contact,
        'example': "add-contact 'name'",
        'description': 'Add new contact name',
    },
    'add-phone': {
        'function': add_phone,
        'example': "add-phone 'name' 'newPhone'",
        'description': 'Add new phone (10-digits number) for contact by name',
    },
    'show-phones': {
        'function': show_phones,
        'example': "show-phone 'name'",
        'description': 'Show phones for contact by name',
    },
    'add-birthday': {
        'function': add_birthday,
        'example': "add-birthday 'name' 'birthday'",
        'description': 'Add birthday (DD.MM.YYYY) for contact by name',
    },
    'show-birthday': {
        'function': show_birthday,
        'example': "show-birthday 'name'",
        'description': 'Show birthday for contact by name',
    },
}

def handle_command(command, args, book):
    if command in command_info:
        command_function = command_info[command]['function']
        if command_function:
            return command_function(args, book)
        else:
            return print("Invalid command. Use 'help' command for Help!")
    else:
        return print("Invalid command. Use 'help' command for Help!")
