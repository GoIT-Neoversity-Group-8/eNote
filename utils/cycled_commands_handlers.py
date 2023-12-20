from cgitb import handler
from constants.messages import command_messages
from utils.input_handlers import parse_input
from app.Record import Record

def cycled_command_handler(record: Record):
    cycled_command_fields = [
        { 
            "text": command_messages["enter_phone"],
            "handler": record.add_phone # TODO
        },
        { 
            "text": command_messages["enter_email"],
            "handler": record.add_note # TODO
        },
        { 
            "text": command_messages["enter_address"],
            "handler": record.add_note # TODO
        },
        { 
            "text": command_messages["enter_birthday"],
            "handler": record.add_note # TODO
        },
        { 
            "text": command_messages["enter_note"],
            "handler": record.add_note # TODO
        },
        { 
            "text": command_messages["enter_tag"],
            "handler": record.add_note # TODO
        },
    ]

    current_field = 0
    while True:
        user_input = input(cycled_command_fields[current_field]["text"])        
        value, *args = parse_input(user_input)

        if value == 'e':
            break
        elif value == 'n':
            if (current_field + 1) == len(cycled_command_fields):
                break
            current_field += 1
            continue
        else:
            field_handler = cycled_command_fields[current_field]["handler"]
            is_updated = field_handler(value)
            if is_updated:
                current_field += 1
