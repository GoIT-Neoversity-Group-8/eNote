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
        
    @input_error()
    def delete_phone(self, phone_to_del):
        phone_to_del = Phone(phone_to_del)
        if phone_to_del.value:
            if str(phone_to_del.value) in [str(p.value) for p in self.phones]:
                self.phones.remove(phone_to_del)
                return True # видалено успішно
        else:
            raise IndexError(error_messages["phone_not_exist"])        
        return False
        
    def add_birthday(self, date):
        birthday = Birthday(date)
        if birthday.value:
            self.birthday = birthday       
        return bool(birthday.value)    
    
    def add_note_message(self, message, *args):
        msg = f"{message} {' '.join(args)}"
        if self.note is None:
            self.note = Note()
            self.note.set_message(msg)
        else:
            self.note.set_message(msg)
        return True
    
    def add_note_tag(self, tag, *args):
        if self.note is None:
            self.note = Note()
            self.note.set_tag(tag)
        else:
            self.note.set_tag(tag)
        return True

    def delete_note(self):
        if self.note:
            self.note = None

    
    