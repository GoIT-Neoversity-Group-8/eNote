from collections import UserDict
from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages, command_messages
from app.Fields import Phone, Birthday, Address, Email, Note
from app.Record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        # TODO self.load_data()

    def find(self, name):        
        return self.data.get(name)

    def add_contact(self, name, phone=None):
        if name in self.data:
            print(error_messages["exist_contact"])
            return
        self.data[name] = Record(name, phone)
        # print(f"{command_messages['contact_added']}")

    def update_contact(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        if name not in self.data:
            print(error_messages["no_contacts"])
            return
        
        try:
            contact = self.data.get(name)

            if contact:
                contact.phone = Phone(phone) if phone else contact.phone
                contact.birthday = Birthday(birthday) if birthday else contact.birthday
                contact.email = Email(email) if email else contact.email
                contact.address = Address(address) if address else contact.address
                contact.note = Note(note) if note else contact.note
                # TODO зберігаємо одразу???
                print(f"Contact {name} has been updated.")
        except ValueError as e:
            print(e)

    
    def find_notes_by_tag(self, tag):
        notes = []
        for name, record in self.data.items():
            if record.note and record.note.tag == tag.strip().upper():
                notes.append({"name": name, "message": record.note.message})

        notes.sort(key=lambda x: x["name"].lower())
        return notes    
    
    def find_notes(self, search_term):
        notes = []
        search_term = search_term.lower()
        for name, record in self.data.items():
            if record.note and (search_term in record.note.tag.lower() or search_term in record.note.message.lower()):
                notes.append({"name": name, "tag": record.note.tag, "message": record.note.message})
        
        notes.sort(key=lambda x: x["tag"].lower())
        return notes

    def add_phone(self, name, new_phone):
        contact = self.data.get(name)
        if contact:
            # Додаємо новий телефонний номер контакту
            contact.phones.append(
                Phone(new_phone)  # Використовуємо клас Phone для валідації
            )
            # TODO зберігаємо одразу???
            print(f"Phone number updated for {name}.")
        else:
            print("Contact not found.")
