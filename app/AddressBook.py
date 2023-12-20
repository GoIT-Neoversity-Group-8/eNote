from collections import UserDict
from utils.prompt_handlers import is_yes_prompt
from utils.cycled_commands_handlers import cycled_command_handler
from constants.messages import error_messages, command_messages
from app.Fields import Phone, Birthday, Address, Email, Note
from app.Record import Record

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        # TODO self.load_data()

    def find(self, name):        
        return self.data.get(name)

    def add_contact(self, name):
        if name in self.data:
            if is_yes_prompt(command_messages["prompt_edit_contact"].format(name)):
                record = self.data[name]
        else:
            record = Record(name)
            self.data[name] = record
        
        if bool(record):
            cycled_command_handler(record)

    def update_contact(self, name):
        record = None
        if name in self.data:
            record = self.data[name]
        else:
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name)):
                record = Record(name)
                self.data[name] = record

        if bool(record):
            cycled_command_handler(record)

    
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
            print(error_messages["no_contact"])
