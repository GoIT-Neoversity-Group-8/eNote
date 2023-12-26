""""Main class AddressBook."""
import json
import os
from collections import UserDict
from datetime import datetime, timedelta
from copy import deepcopy
from eNote.utils.error_handlers import input_error
from eNote.utils.prompt_handlers import is_yes_prompt
from eNote.utils.cycled_commands_handlers import cycled_command_handler
from eNote.constants.messages import error_messages, command_messages
from eNote.app.Record import Record
from eNote.app.Fields import Note

home_path = os.path.expanduser("~")
file_path = os.path.join(home_path, 'contacts.json')
class AddressBook(UserDict):
    """Main class for addressbook.

    load_data=True - по замочуванню при створенні об'єкта - завантажуються
    збережені контакти із файлу"""
    def __init__(self, load_data=True):
        super().__init__()
        if load_data:
            self.load_data()

    # -- contact
    def find(self, name):
        """Find contact by name"""
        return self.data.get(name)

    def add_contact(self, name):
        """Add new  contact"""
        record = None
        if name in self.data:
            if is_yes_prompt(command_messages["prompt_edit_contact"].format(name=name)):
                record = self.data[name]
        else:
            record = Record(name)
            self.data[name] = record
        if bool(record):
            cycled_command_handler(record)
            return True

    @input_error()
    def update_contact(self, name):
        """Update contact in loop."""
        record = None
        if name in self.data:
            record = self.data[name]
            is_edit_contact = True
        else:
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name=name)):
                record = Record(name)
                self.data[name] = record
                is_edit_contact = False
        if bool(record):
            cycled_command_handler(record, is_edit_contact)
            return True

    @input_error()
    def rename(self, name, new_name):
        """Update contact in loop."""
        record = None
        if new_name in self.data.keys():
            raise ValueError(error_messages["exist_contact"])
        else:
            record = Record(new_name, self.data[name].phone_str_list, self.data[name].birthday.value, self.data[name].email, self.data[name].address, self.data[name].note)
            # record[new_name] = deepcopy(self.data[name][name])
            self.data[new_name] = record
            del self.data[name]
            return True

    @input_error()
    def delete_contact(self, name):
        """Delete contact by name."""
        deleted = self.data.pop(name, None)
        if not deleted:
            raise KeyError(error_messages["no_contact"])
        return True

    # -- note
    def add_note(self, name):
        """Add note to contact."""
        record = None
        if name in self.data:
            record = self.data[name]
        else:
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name=name)):
                record = Record(name)
                self.data[name] = record

        if bool(record):
            cycled_command_handler(record, is_note=True)
            return True
        else:
            return False

    # -- phone
    @input_error()
    def add_phone(self, name, phone):
        record: Record = None
        if name in self.data:
            record = self.find(name)
        else:
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name=name)):
                record = Record(name)
                self.data[name] = record
        if record:
            return record.add_phone(phone)

    @input_error()
    def edit_phone(self, name, old_phone, new_phone):
        record: Record = None
        if not name in self.data:
            raise KeyError(error_messages["no_contact"])
        else:
            record = self.find(name)
        if record:
            return record.edit_phone(old_phone, new_phone)

    @input_error()
    def delete_phone(self, name, phone_to_del):
        if name in self.data:
            record: Record = self.find(name)
            return record.delete_phone(phone_to_del)
        else: # контакту з таким іменем немає
            raise IndexError(error_messages["name_not_found"])

    @input_error()
    def show_phones(self, name):
        if not name in self.data:
            raise KeyError(error_messages["no_contact"])
        else:
            return self.data[name].phones

    # -- email
    @input_error()
    def add_email(self, name, email):
        record: Record = None
        if name in self.data:
            record = self.find(name)
        else:
            if is_yes_prompt(command_messages["prompt_add_contact"].format(name=name)):
                record = Record(name)
                self.data[name] = record
        if record:
            return record.add_email(email)

    @input_error()
    def edit_email(self, name, email):
        if not name in self.data:
            raise KeyError(error_messages["no_contact"])
        else:
            record: Record = self.find(name)
            return record.add_email(email)

    @input_error()
    def delete_email(self, name):
        if not name in self.data:
            raise KeyError(error_messages["no_contact"])
        else:
            record: Record = self.find(name)
            return record.delete_email()

    # -- address
    @input_error()
    def add_address(self, name, address, *args):
        if not name in self.data:
            raise KeyError(error_messages["no_contact"])
        else:
            record: Record = self.find(name)
            return record.add_address(address, *args)

    @input_error()
    def delete_address(self, name):
        if not name in self.data:
            raise KeyError(error_messages["no_contact"])
        else:
            record: Record = self.find(name)
            return record.delete_address()

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
        found_contacts = AddressBook(load_data=False)
        search_term = search_term.lower()
        contact: Record
        for name, contact in self.data.items():
            # Перевірка, чи пошуковий термін міститься в будь-якому з атрибутів контакту
            if (
                search_term in contact.name.value.lower()
                or (contact.phones and search_term in contact.phones_str)
                or (contact.email and search_term in contact.email.value.lower())
                or (contact.address and search_term in contact.address.value.lower())
                or (contact.birthday and search_term == contact.birthday.value.lower())
                or (contact.note and search_term in contact.note.message.lower())
                or (contact.note and search_term in contact.note.tag.lower())
            ):
                found_contacts[name] = contact
        return found_contacts

    def save_data(self):
        """Save address book to file."""
        with open(file_path, 'w', encoding="utf-8") as file:
            json_data = {}
            for name, contact in self.data.items():
                json_data[name] = {
                    "name": contact.name.value,
                    "phones": contact.phone_str_list,
                    "email": contact.email.value if contact.email else None,
                    "address": contact.address.value if contact.address else None,
                    "birthday": contact.birthday.value if contact.birthday else None,
                    "note": contact.note.to_dict() if contact.note else None
                }
            json.dump(json_data, file)

    def load_data(self):
        """Load address book from file."""
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                json_data = json.load(file)
                for name, contact_data in json_data.items():
                    self.data[name] = Record(
                        name=contact_data['name'],
                        phones=contact_data['phones'],
                        email=contact_data['email'],
                        address=contact_data['address'],
                        birthday=contact_data['birthday'],
                        note=Note.from_dict(contact_data['note']) if 'note' in contact_data and contact_data['note'] is not None else None
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}
