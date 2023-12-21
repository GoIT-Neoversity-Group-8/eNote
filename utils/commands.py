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
        'example': "add-contact 'John' '1234567890' '15.04.2000' 'john@example.com' '123 Main St'",
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
    'show-phone': {
        'function': show_phones,
        'example': "show-phone 'name'",
        'description': command_descriptions["show_phones"],
        'parameters': ['{name}'],
    },
    'add-birthday': {
        'function': add_birthday,
        'example': "add-birthday 'John' '01-01-1990'",
        'description': command_descriptions["add_birthday"],
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
        'example': "update-contact 'John' '123-456-7890' '01-01-1990' 'john@example.com' '123 Main St'",
        'description': command_descriptions["update_contact"],
        'parameters':  ['{name}','{newPhone}','{birthday}','{email}','{addres}'],
    },
    'delete-contact': {
        'function': delete_contact,
        'example': "delete-contact 'John'",
        'description': command_descriptions["delete_contact"],
        'parameters': ['{name}'],
    },
    'add-note': {
        'function': add_note,
        'example': "add-note 'John' 'Reminder' 'Meeting at 5 PM'",
        'description': command_descriptions["add_note"],
        'parameters': ['{name}', '{tag}', '{message}'],
    },
    'edit-note': {
        'function': add_note,
        'example': "edit-note 'John' 'Reminder' 'Updated meeting at 6 PM'",
        'description': command_descriptions["edit_note"],
        'parameters': ['{name}', '{tag}', '{message}'],
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
            return print(error_messages["invalid_command"])
    else:
        return print(error_messages["invalid_command"])
