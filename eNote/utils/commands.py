from eNote.app.command_handlers import *
from eNote.constants.messages import *
from eNote.utils.print_handlers import *
from tabulate import tabulate

def bot_help(args, book):
    print_hint(command_messages["commands"])

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
    print(tabulate(hlp_tbl, hlp_tbl_headers, tablefmt="rounded_grid"))

command_info = {
    'help': {
        'function': bot_help,
        'example': None,
        'description': command_descriptions["help"],
        'parameters': None,
    },
    'hello': {
        'function': bot_hello,
        'example': None,
        'description': command_descriptions["hello"],
        'parameters': None,
    },
    'exit': {
        'function': None,  # No function associated with exit, it will be handled separately
        'example': None,
        'description': command_descriptions["exit"],
        'parameters': None,
    },
    'close': {
        'function': None,  # No function associated with exit, it will be handled separately
        'example': None,
        'description': command_descriptions["exit"],
        'parameters': None,
    },
    'all': {
        'function': show_all,
        'example': None,
        'description': command_descriptions["show_all"],
        'parameters': None,
    },
    'add-contact': {
        'function': add_contact,
        'example': "add-contact 'John Doe' | add-contact John",
        'description': command_descriptions["add_contact"],
        'parameters': ['{name}'],
    },
    'find': {
        'function': find_contact,
        'example': "find 'John' | find 1231234444",
        'description': command_descriptions["find"],
        'parameters': ['{search_word}'],
    },
    'add-phone': {
        'function': add_phone,
        'example': "add-phone 'John Doe' '0501234455'",
        'description': command_descriptions["add_phone"],
        'parameters': ['{name}','{newPhone}'],
    },
    'edit-phone': {
        'function': edit_phone,
        'example': "edit-phone 'John Doe' '0501234455' '0501234355'",
        'description': command_descriptions["edit_phone"],
        'parameters': ['{name}','{oldPhone}','{newPhone}'],
    },
    'delete-phone': {
        'function': delete_phone,
        'example': "delete-phone 'John Doe' '0501234455'",
        'description': command_descriptions["delete_phone"],
        'parameters': ['{name}','{phone}'],
    },
    'show-phone': {
        'function': show_phones,
        'example': "show-phone 'name'",
        'description': command_descriptions["show_phones"],
        'parameters': ['{name}'],
    },
    'add-email': {
        'function': add_email,
        'example': "add-email 'John Doe' 'john@doe.com'",
        'description': command_descriptions["add_email"],
        'parameters': ['{name}','{email}'],
    },
    'edit-email': {
        'function': edit_email,
        'example': "edit-email 'John Doe' 'john@doe.com'",
        'description': command_descriptions["edit_email"],
        'parameters': ['{name}','{newEmail}'],
    },
    'delete-email': {
        'function': delete_email,
        'example': "delete-email 'John Doe'",
        'description': command_descriptions["delete_email"],
        'parameters': ['{name}','{email}'],
    },
     'add-address': {
        'function': add_address,
        'example': "add-address 'John Doe' 'Осьо Туть'",
        'description': command_descriptions["add_address"],
        'parameters': ['{name}','{address}'],
    },
    'edit-address': {
        'function': add_address,
        'example': "edit-address 'John Doe' 'А тепер Туть'",
        'description': command_descriptions["edit_address"],
        'parameters': ['{name}','{newAddress}'],
    },
    'delete-address': {
        'function': delete_address,
        'example': "delete-address 'John Doe'",
        'description': command_descriptions["delete_address"],
        'parameters': ['{name}'],
    },
    'add-birthday': {
        'function': add_birthday,
        'example': "add-birthday 'John' '20.01.1990'",
        'description': command_descriptions["add_birthday"],
        'parameters': ['{name}','{birthday}'],
    },
    'update-birthday': {
        'function': add_birthday,
        'example': "update-birthday 'John' '20.01.1990'",
        'description': command_descriptions["update_birthday"],
        'parameters': ['{name}','{birthday}'],
    },
    'show-birthday': {
        'function': show_birthday,
        'example': "show-birthday 'John'",
        'description': command_descriptions["show_birthday"],
        'parameters': ['{name}'],
    },
    'show-birthdays': {
        'function': show_birthdays,
        'example': "show-birthdays",
        'description': command_descriptions["show_birthdays"],
        'parameters': None,
    },
    'find-birthdays': {
        'function': find_birthdays,
        'example': "find-birthdays 5",
        'description': command_descriptions["find_birthdays"],
        'parameters': ['{days}'],
    },
    'update-contact': {
        'function': update_contact,
        'example': "update-contact 'John Doe'",
        'description': command_descriptions["update_contact"],
        'parameters':  ['{name}'],
    },
    'delete-contact': {
        'function': delete_contact,
        'example': "delete-contact 'John'",
        'description': command_descriptions["delete_contact"],
        'parameters': ['{name}'],
    },
    'add-note': {
        'function': add_note,
        'example': "add-note 'John'",
        'description': command_descriptions["add_note"],
        'parameters': ['{name}'],
    },
    'update-note': {
        'function': edit_note,
        'example': "edit-note 'John'",
        'description': command_descriptions["edit_note"],
        'parameters': ['{name}'],
    },
    'find-notes-by-tag': {
        'function': find_note_by_tag,
        'example': "find-notes-by-tag 'Reminder'",
        'description': command_descriptions["find_note_by_tag"],
        'parameters': ['{tag}'],
    },
    'find-notes': {
        'function': find_notes,
        'example': "find-notes 'search text'",
        'description': command_descriptions["find_notes"],
        'parameters': ['{search text}'],
    },
    'delete-note': {
        'function': delete_note,
        'example': "fdelete-note 'John'",
        'description': command_descriptions["delete_note"],
        'parameters': ['{name}'],
    },
}

# Ordered dictionary for command_info data
command_dict = dict(sorted(command_info.items()))
# List of available commands
command_keys = list(command_dict.keys())
# Dictionary of parameters for each command
command_parameters = {key: value['parameters'] for key, value in command_dict.items() if value['parameters'] is not None}

def handle_command(command, args, book):
    if command in command_info:
        command_function = command_info[command]["function"]
        if command_function:
            return command_function(args, book)
        else:
            return print_error(error_messages["invalid_command"])
    else:
        return print_error(error_messages["invalid_command"])
