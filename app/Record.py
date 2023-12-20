from app.Fields import Name, Phone, Email, Address, Birthday, Note, Tag

class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        self.name = Name(name)
        self.phones = [Phone(phone),] if phone else []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None
        self.note = Note(note) if note else None

    def add_note(self, note):
        #TODO Note
        print("#TODO add_note(self, note)")
        pass

    def update_note(self, new_note):
        #TODO Note
        print("#TODO update_note(self, new_note)")
        pass