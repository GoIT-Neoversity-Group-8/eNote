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

    def add_contact(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        if name in self.data:
            print(error_messages["exist_contact"])
            return False
        self.data[name] = Record(name, phone, birthday, email, address, note)
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
                # print(f"Contact {name} has been updated.")
        except ValueError as e:
            print(e)

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

    def add_phone(self, name, new_phone):
        contact = self.data.get(name)
        if contact:
            # Додаємо новий телефонний номер контакту
            contact.phones.append(
                Phone(new_phone)  # Використовуємо клас Phone для валідації
            )
            # TODO зберігаємо одразу???
            # print(f"Phone number updated for {name}.")
        else:
            print(error_messages["no_contact"])
