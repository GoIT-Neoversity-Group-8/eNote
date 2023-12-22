from app.Fields import Name, Phone, Email, Address, Birthday, Note, Tag
from constants.messages import error_messages, validation_messages
from utils.error_handlers import input_error
from utils.validators import is_valid_phone

class Record:
    def __init__(self, name, phones=None, birthday=None, email=None, address=None, note=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in (phones or [])]
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None
        self.note = note if note else None

    # -- phones
    @property
    def phone_str_list(self):
        return list(map(str, self.phones))

    @property
    def phones_str(self):
        return ', '.join(self.phone_str_list)

    @input_error()
    def add_phone(self, new_phone):
        phone = Phone(new_phone)
        if phone.value:
            if new_phone in self.phone_str_list:
                raise ValueError(error_messages["phone_exist"])
            else:
                self.phones.append(phone)
                # self.phones.sort() # - error
                return True

    @input_error()
    def edit_phone(self, old_phone, new_phone):
        if not old_phone in self.phone_str_list:
            raise ValueError(error_messages["phone_not_exist"])
        else:
            phone = Phone(new_phone)
            if phone.value:
                index = self.phone_str_list.index(old_phone)
                self.phones[index] = phone
                return True
        
    @input_error()
    def delete_phone(self, phone_to_del):
        if not is_valid_phone(phone_to_del):
            raise ValueError(validation_messages["invalid_phone"])
        else:
            if phone_to_del in self.phone_str_list:
                index = self.phone_str_list.index(phone_to_del)
                self.phones.pop(index, None)
                return True
            else:
                raise IndexError(error_messages["phone_not_exist"])

    # -- email
    def add_email(self, email):
        email = Email(email)
        if email.value:
            # TODO need to check if email exists ?
            self.email = email
            return True
    
    def delete_email(self):
        self.email = None
        return True

    # -- address
    def add_address(self, address, *args):
        self.address = Address(f"{address} {' '.join(args)}")
        return True
    
    def delete_address(self):
        self.address = None
        return True

    # -- birthday 
    def add_birthday(self, date):
        birthday = Birthday(date)
        if birthday.value:
            self.birthday = birthday
        return bool(birthday.value)
    
    # -- notes
    def add_note_message(self, message, *args):
        msg = f"{message} {' '.join(args)}"
        if self.note is None:
            self.note = Note()
        self.note.set_message(msg)
        return True
    
    def add_note_tag(self, tag, *args):
        if self.note is None:
            self.note = Note()
        self.note.set_tag(tag)
        return True

    def delete_note(self):
        if self.note:
            self.note = None
