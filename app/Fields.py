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
        pass

class Phone(Field):
    def __init__(self, phone):
        pass

class Birthday(Field):
    def __init__(self, date):
        pass

class Note(Field):
    def __init__(self, note):
        pass

class Tag(Field):
    def __init__(self, tag):
        pass
