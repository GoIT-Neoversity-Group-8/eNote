from app.command_handlers import *
from constants.messages import *

def bot_help(args, book):
    print(command_messages["commands"])
    print("|{:_^15}|{:_^45}|{:_^60}|".format(
        help_table_messages["command_col"], 
        help_table_messages["example_col"], 
        help_table_messages["description_col"],
    ))
    for command, info in command_info.items():
        description = info['description']
        example = info['example']
        print("|{:<15}|{:<45}|{:<60}|".format(command, (' ' if example is None else f'example: {example}'), description))
    print("\n")

command_info = {
    'help': {
        'function': bot_help,
        'example': None,
        'description': command_descriptions["help"],
    },
    'hello': {
        'function': bot_hello,
        'example': None,
        'description': command_descriptions["hello"],
    },
    'exit, close': {
        'function': None,  # No function associated with exit, it will be handled separately
        'example': None,
        'description': command_descriptions["exit"],
    },
    'all': {
        'function': show_all,
        'example': None,
        'description': command_descriptions["show_all"],
    },
    'add-contact': {
        'function': add_contact,
        'example': "add-contact <name>",
        'description': command_descriptions["add_contact"],
    },
    'add-phone': {
        'function': add_phone,
        'example': "add-phone <name> <new phone>",
        'description': command_descriptions["add_phone"],
    },
    'show-phones': {
        'function': show_phones,
        'example': "show-phone <name>",
        'description': command_descriptions["show_phones"],
    },
    'add-birthday': {
        'function': add_birthday,
        'example': "add-birthday <name> <birthday>",
        'description': command_descriptions["add_birthday"],
    },
    'show-birthday': {
        'function': show_birthday,
        'example': "show-birthday <name>",
        'description': command_descriptions["show_birthday"],
    },
}

def handle_command(command, args, book):
    if command in command_info:
        command_function = command_info[command]['function']
        if command_function:
            return command_function(args, book)
        else:
            return print(error_messages["invalid_command"])
    else:
        return print(error_messages["invalid_command"])
