from eNote.constants.messages import command_messages
from eNote.utils.input_handlers import parse_input
from eNote.app.Record import Record
from eNote.utils.print_handlers import print_hint

BLUE = "\033[94m"
RESET = "\033[0m"

def cycled_command_handler(record: Record, is_edit_contact = False, is_note = False):
    cycled_command_fields = [        
        { 
            "text": command_messages["enter_note"],
            "handler": record.add_note_message
        },
        { 
            "text": command_messages["enter_tag"],
            "handler": record.add_note_tag
        },
    ] if is_note else [
        { 
            "text": command_messages["enter_phone"],
            "handler": record.edit_phone if is_edit_contact else record.add_phone
        },
        { 
            "text": command_messages["enter_email"],
            "handler": record.add_email # TODO
        },
        { 
            "text": command_messages["enter_address"],
            "handler": record.add_address # TODO
        },
        { 
            "text": command_messages["enter_birthday"],
            "handler": record.add_birthday
        },
    ]
    
    print_hint(f'  {command_messages["cycle_hint_note"] if is_note else command_messages["cycle_hint_contact"]}')

    current_field = 0
    while True:
        if (current_field) == len(cycled_command_fields):
            break

        user_input = input(
            BLUE + '    ' + 
            cycled_command_fields[current_field]["text"] +
            RESET
        )

        value, *args = [None]
        if bool(user_input.strip()):
            value, *args = parse_input(user_input)

        if value == 'e':
            break
        elif not value or value == 'n':            
            current_field += 1
            continue
        else:
            field_handler = cycled_command_fields[current_field]["handler"]
            is_updated = field_handler(value, *args)
            if is_updated:
                current_field += 1
