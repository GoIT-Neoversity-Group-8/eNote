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

    def add_note(self, note):
        #TODO Note
        print("#TODO add_note(self, note)")
        return True

    def update_note(self, new_note):
        #TODO Note
        print("#TODO update_note(self, new_note)")
        pass
    