from utils.validators import is_valid_phone, is_valid_date
from utils.error_handlers import input_error, validation_error, ValidationError
from constants.messages import error_messages, validation_messages

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, phone):       
        self.value = None
        self.set_value(phone)

    @validation_error
    def set_value(self, phone):
        if not is_valid_phone(phone):
            raise ValidationError(validation_messages["invalid_phone"])
        else:
            self.value = Field(phone)

    def __eq__(self, other: object) -> bool:
        return self.value.value == other.value.value

    def __ne__(self, other: object) -> bool:
        return self.value.value != other.value.value
    
    def __lt__(self, other: object) -> bool:
        return int(self.value.value) < int(other.value.value)

    def __gt__(self, other: object) -> bool:
        return int(self.value.value) > int(other.value.value)

    def __le__(self, other: object) -> bool:
        return int(self.value.value) <= int(other.value.value)

    def __ge__(self, other: object) -> bool:
        return int(self.value.value) >= int(other.value.value)

class Email:
    def __init__(self, email):
        pass

class Address:
    def __init__(self, address):
        pass

class Birthday(Field):
    def __init__(self, date):
        self.value = None
        self.set_value(date)
    
    @validation_error
    def set_value(self, date):
        if not is_valid_date(date):
            raise ValidationError(validation_messages["invalid_date"])
        else:
            self.value = Field(date)

class Note():
    def __init__(self, tag='', message=''):
        self.tag = tag.strip().upper()
        self.message = message

    def set_message(self, message):
        self.message = message

    def set_tag(self, tag):
        self.tag = tag.strip().upper()

    def __str__(self):
        return f"Tag: {self.tag}, Message: {self.message}"

class Tag(Field):
    def __init__(self, tag):
        pass
