from app.command_handlers import *
from constants.messages import *
from tabulate import tabulate


def bot_help(args, book):
    print(command_messages["commands"])

    # Prepare Help table
    hlp_tbl_headers = [
        help_table_messages["command_col"],
        help_table_messages["example_col"],
        help_table_messages["description_col"],
    ]
    hlp_tbl = [
        [command, info["example"], info["description"]]
        for command, info in command_dict.items()
    ]
    # Print Help table
    print(tabulate(hlp_tbl, hlp_tbl_headers, tablefmt="rounded_outline"))


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
        'example': "add-contact 'John Doe' '123-456-7890' '01-01-1990' 'john@example.com' '123 Main St'",
        'description': command_descriptions["add_contact"],
    },
    'find': {
        'function': find_contact,
        'example': "find-contact 'John'",
        'description': 'Find contacts by various criteria such as name, phone, email, address, or birthday.',
    },
    'add-phone': {
        'function': add_phone,
        'example': "add-phone 'John Doe' '987-654-3210'",
        'description': command_descriptions["add_phone"],
    },
    'show-phone': {
        'function': show_phones,
        'example': "show-phone 'name'",
        'description': command_descriptions["show_phones"],
    },
    'add-birthday': {
        'function': add_birthday,
        'example': "add-birthday 'John Doe' '01-01-1990'",
        'description': command_descriptions["add_birthday"],
    },
    'show-birthday': {
        'function': show_birthday,
        'example': "show-birthday 'John Doe'",
        'description': command_descriptions["show_birthday"],
    },
    'show-birthdays': {
        'function': show_birthdays,
        'example': "show-birthdays",
        'description': command_descriptions["show_birthdays"],
    },
    'find-birthdays': {
        'function': find_birthdays,
        'example': "find-birthdays 5",
        'description': command_descriptions["find_birthdays"]
    },
    'update-contact': {
        'function': update_contact,
        'example': "update-contact 'John Doe' '123-456-7890' '01-01-1990' 'john@example.com' '123 Main St'",
        'description': command_descriptions["update_contact"],
    },
    'delete-contact': {
        'function': delete_contact,
        'example': "delete-contact 'John Doe'",
        'description': command_descriptions["delete_contact"],
    },
    'add-note': {
        'function': add_note,
        'example': "add-note 'John Doe' 'Meeting at 5 PM'",
        'description': command_descriptions["add_note"],
    },
    'edit-note': {
        'function': add_note,
        'example': "edit-note 'John Doe' 0 'Updated meeting at 6 PM'",
        'description': command_descriptions["edit_note"],
    },
}

command_dict= dict(sorted(command_info.items()))

def handle_command(command, args, book):
    if command in command_info:
        command_function = command_info[command]["function"]
        if command_function:
            return command_function(args, book)
        else:
            return print(error_messages["invalid_command"])
    else:
        return print(error_messages["invalid_command"])
