from utils.validators import is_valid_phone, is_valid_date
from utils.error_handlers import input_error, validation_error, ValidationError
from constants.messages import error_messages, validation_messages


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        if not is_valid_phone(phone):
            raise ValueError(error_messages["invalid_phone_format"])
        self.value = phone


class Email:
    def __init__(self, email):
        pass


class Address:
    def __init__(self, address):
        pass


class Birthday(Field):
    def __init__(self, date):
        pass


class Note():
    def __init__(self, tag, message):
        self.tag = tag.strip().upper()
        self.message = message


class Tag(Field):
    def __init__(self, tag):
        pass
