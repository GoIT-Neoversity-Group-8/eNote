from app.Fields import Name, Phone, Email, Address, Birthday, Note, Tag

class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        self.name = Name(name)
        self.phones = [Phone(phone),] if phone else []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None
        self.note = Note(note) if note else None

    def add_note(self, tag, message):
        if self.note is None:
            self.note = Note(tag, message)            
        else:
            self.note.tag = tag.strip().upper()
            self.note.message = message

    
    def delete_note(self):
        if self.note:
            self.note = None
    