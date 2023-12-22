from collections import UserDict
from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from utils.cycled_commands_handlers import cycled_command_handler
from constants.messages import error_messages, command_messages
from app.Record import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        # TODO self.load_data()

    # -- contact
    def find(self, name):        
        return self.data.get(name)

    def add_contact(self, name):
        if name in self.data:
            if is_yes_prompt(command_messages["prompt_edit_contact"].format(name=name)):
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
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name=name)):
                record = Record(name)
                self.data[name] = record

        if bool(record):
            cycled_command_handler(record)

    def delete_contact(self, name):
        return self.data.pop(name, None)

    # -- phone
    @input_error()
    def add_phone(self, name, phone):
        record = None
        if name in self.data:
            record = self.find(name)
        else:
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name=name)):
                record = Record(name)
                self.data[name] = record
        if record:
            return record.add_phone(phone)
    
    @input_error(error_messages["no_contact"])
    def show_phones(self, name):
        if not name in self.data:
            raise KeyError()
        else:
            return self.data[name].phones
    
    # -- notes
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
    
    # -- birthdays
    def show_birthdays(self):
        data = []
        for name, record in self.data.items():
            if record.birthday and str(record.birthday):
                data.append({
                    "name": name, 
                    "birthday": str(record.birthday)
                })
        
        data.sort(key=lambda x: x["name"].lower())
        return data
    
    def find_birthdays_in_days(self, days):
        birthdays = {}
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)

        for name, record in self.data.items():
            birthday_str = str(record.birthday) if (record.birthday and record.birthday.value) else None
            if birthday_str:
                birthday = datetime.strptime(birthday_str, '%d.%m.%Y')                    
                birthday_this_year = birthday.replace(year=current_date.year, month=birthday.month, day=birthday.day)
                birthday_next_year = birthday_this_year.replace(year=current_date.year + 1)
                    
                if current_date <= birthday_this_year <= future_date:                       
                    if not birthday_this_year.date() in birthdays:
                        birthdays[birthday_this_year.date()] = []
                    birthdays[birthday_this_year.date()].append(name)
                   
                if current_date <= birthday_next_year <= future_date:
                    if not birthday_next_year.date() in birthdays:
                        birthdays[birthday_next_year.date()] = []
                    birthdays[birthday_next_year.date()].append(name)

        sorted_birthdays = dict(sorted(birthdays.items()))
        return sorted_birthdays

    # -- complex search
    def find_contact(self, search_term: str):
        found_contacts = {}
        search_term = search_term.lower()
        contact: Record
        for name, contact in self.data.items():
            # Перевірка, чи пошуковий термін міститься в будь-якому з атрибутів контакту
            if (
                search_term in contact.name.value.lower()
                or (contact.phones and search_term in map(str,contact.phones))
                # TODO доробити пошук коли будуть готові поля
                # or (contact.email and search_term in contact.email.value.lower())
                # or (contact.address and search_term in contact.address.value.lower())
                # or (contact.birthday and search_term == contact.birthday.value.lower())
                # or (contact.note and search_term in contact.note.value.lower())
                ):
                found_contacts[name] = contact
        return found_contacts
