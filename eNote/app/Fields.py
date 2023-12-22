from utils.validators import is_valid_email, is_valid_phone, is_valid_date
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
            self.value = phone

class Email(Field):
    def __init__(self, email):
        self.value = None
        self.set_value(email)

    @validation_error
    def set_value(self, email):
        if not is_valid_email(email):
            raise ValidationError(validation_messages["invalid_email"])
        else:
            self.value = email

class Address(Field):
    def __init__(self, address):
        self.value = address

class Birthday(Field):
    def __init__(self, date):
        self.value = None
        self.set_value(date)
    
    @validation_error
    def set_value(self, date):
        if not is_valid_date(date):
            raise ValidationError(validation_messages["invalid_date"])
        else:
            self.value = date

class Note():
    def __init__(self):
        self.tag = ''
        self.message = ''

    def set_message(self, message):
        self.message = message

    def set_tag(self, tag):
        self.tag = tag.strip().upper()

    def __str__(self):
        return f"Tag: {self.tag}, Message: {self.message}"
    
    def to_dict(self):
        return {
            'tag': self.tag,
            'message': self.message
        }

    @classmethod
    def from_dict(cls, data):
        note_instance = cls()
        note_instance.tag = data['tag']
        note_instance.message = data['message']
        return note_instance

class Tag(Field):
    def __init__(self, tag):
        pass
