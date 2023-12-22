from constants.messages import command_messages
from utils.input_handlers import parse_input
from app.Record import Record

BLUE = "\033[94m"
RESET = "\033[0m"

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
            "handler": record.add_birthday
        },
        { 
            "text": command_messages["enter_note"],
            "handler": record.add_note # TODO
        },
        # { 
        #     "text": command_messages["enter_tag"],
        #     "handler": record.add_note # TODO
        # },
    ]

    current_field = 0
    while True:
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
            if (current_field + 1) == len(cycled_command_fields):
                break
            current_field += 1
            continue
        else:
            field_handler = cycled_command_fields[current_field]["handler"]
            is_updated = field_handler(value, *args)
            if is_updated:
                current_field += 1
