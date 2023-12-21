from app.Fields import Name, Phone, Email, Address, Birthday, Note, Tag

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None
        self.note = None
        self.tags = []

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone.value:
            self.phones.append(phone)
        return bool(phone.value)
        
    def add_birthday(self, date):
        birthday = Birthday(date)
        if birthday.value:
            self.birthday = birthday       
        return bool(birthday.value)

    def add_note(self, tag, message):
        if self.note is None:
            self.note = Note(tag, message)            
        else:
            self.note.tag = tag.strip().upper()
            self.note.message = message

    def delete_note(self):
        if self.note:
            self.note = None

    
    