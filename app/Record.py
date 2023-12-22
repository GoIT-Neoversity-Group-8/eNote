from app.Fields import Name, Phone, Email, Address, Birthday, Note, Tag
from constants.messages import error_messages
from utils.error_handlers import input_error

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None
        self.note = None
        self.tags = []

    @input_error()
    def add_phone(self, phone):
        phone = Phone(phone)
        if phone.value:
            if str(phone.value) in [str(p.value) for p in self.phones]:
                raise ValueError(error_messages["phone_exist"])
            self.phones.append(phone)
            self.phones.sort()
        return bool(phone.value)
        
    def add_birthday(self, date):
        birthday = Birthday(date)
        if birthday.value:
            self.birthday = birthday       
        return bool(birthday.value)

    def add_note(self, tag='', message=''):
        if self.note is None:
            self.note = Note(tag, message)            
        else:
            self.note.tag = tag.strip().upper()
            self.note.message = message
        return True

    def delete_note(self):
        if self.note:
            self.note = None

    
    