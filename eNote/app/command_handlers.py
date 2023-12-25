from tabulate import tabulate
from eNote.utils.error_handlers import input_error
from eNote.constants.messages import error_messages, command_messages
from eNote.app.AddressBook import AddressBook
from eNote.utils.validators import *
from eNote.utils.print_handlers import *
from eNote.app.Record import Record

def bot_hello(args, book: AddressBook):
    print_hint(command_messages["hello"])

# -- Contact
@input_error(error_messages["no_name"])
def add_contact(args, book: AddressBook):
    name = args[0]
    is_updated = book.add_contact(name)
    if is_updated:
        print_success(command_messages["contact_added"])

@input_error(error_messages["no_name"])
def update_contact(args, book: AddressBook):
    name = args[0]
    is_updated = book.update_contact(name)
    if is_updated:
        print_success(command_messages['contact_updated'].format(name=name))

@input_error(error_messages["no_name"])
def delete_contact(args, book: AddressBook):
    name = args[0]
    if book.delete_contact(name):
        print_success(command_messages['contact_deleted'].format(name=name))

def show_all(args, book: AddressBook):
    if not book.data:
        print(error_messages["no_contacts"])
        return
    # Таблиця контактів
    print_book(book)

# -- Phones
@input_error(error_messages["no_name_and_phone"])
def add_phone(args, book: AddressBook):
    name, phone = args
    if book.add_phone(name, phone):
        print_success(command_messages["phone_added"])

@input_error(error_messages["no_name_and_phones"])
def edit_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    if book.edit_phone(name, old_phone, new_phone):
        print_success(command_messages["phone_updated"])

@input_error(error_messages["no_name_and_phone"])
def delete_phone(args, book: AddressBook):
    name, phone_to_del = args
    if book.delete_phone(name, phone_to_del):
        print_success(command_messages['phone_deleted'].format(name=name, phone=phone_to_del))

@input_error(error_messages["no_name"])
def show_phones(args, book: AddressBook):
    name = args[0]
    phones = book.show_phones(name)
    if phones:
        txt_phones = ", ".join(map(str, phones))
        mess = command_messages['show_phones'].format(name=name)
        print_hint(f"{mess}: {txt_phones}")
    else:
        print_hint(command_messages["no_phones"])

# -- Email
@input_error(error_messages["no_name_and_email"])
def add_email(args, book: AddressBook):
    name, email = args
    if book.add_email(name, email):
        print_success(command_messages["email_added"])

@input_error(error_messages["no_name_and_email"])
def edit_email(args, book: AddressBook):
    name, new_email = args
    if book.edit_email(name, new_email):
        print_success(command_messages["email_updated"])

@input_error(error_messages["no_name"])
def delete_email(args, book: AddressBook):
    name = args[0]
    if book.delete_email(name):
        print_success(command_messages['email_deleted'])

# -- Address
@input_error(error_messages["no_name"])
def add_address(args, book: AddressBook):
    name, address, *data = args
    if book.add_address(name, address, *data):
        print_success(command_messages["address_added"])

@input_error(error_messages["no_name"])
def delete_address(args, book: AddressBook):
    name = args[0]
    if book.delete_address(name):
        print_success(command_messages['address_deleted'])

# -- Birthdays
@input_error(error_messages["no_name_and_birthday"])
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record: Record = book.find(name)
    if not record:
        print_error(error_messages["no_contact"])
    elif record.add_birthday(birthday):
        print_success(command_messages["birthday_added"])

@input_error(error_messages["no_name"])
def show_birthday(args, book: AddressBook):
    name = args[0]
    record: Record = book.find(name)
    if not record:
        print_error(error_messages["no_contact"])
    elif record.birthday and str(record.birthday):
        print_hint(command_messages["show_birthday"].format(birthday=record.birthday.value))
    else:
        print_hint(command_messages["no_birthday"])

def show_birthdays(args, book: AddressBook):
    data = book.show_birthdays()
    if not data:
        print_hint(command_messages["no_birthdays"])
        return    
    
    tbl_header = ["Name", "Birthday"]
    tbl_data = [
        [item["name"], item["birthday"]]
        for item in data
    ]
    tbl_data = tbl_data or ["", ""]
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_outline")
    print(str(tbl))

@input_error(error_messages["no_days"])
def find_birthdays(args, book: AddressBook):    
    days = int(args[0]) if len(args) == 1 else 7    
    birthdays = book.find_birthdays_in_days(days)

    if not birthdays:
        print_hint(command_messages["no_birthdays_in_days"].format(days=days))
        return
    
    tbl_header = ["Date", "Birthday"]
    tbl_data = [
        [date.strftime('%d.%m'), ", ".join(map(str, data))]
        for date, data in birthdays.items()
    ]
    tbl_data = tbl_data or ["", ""]
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_outline")
    print(str(tbl))    

# -- complex search by string
@input_error(error_messages["find_what"])
def find_contact(args, book: AddressBook):
    """Search the contact.

    Search for the specified text in all fields of the contact."""
    #передані параметри вважаємо одним рядком і шукаємо по ньому
    search_term = ' '.join(args).strip()
    if not search_term:
        raise ValueError()
    found_contacts = book.find_contact(search_term)
    if found_contacts: # якщо список знайдених не порожній - показуємо таблицю з результатами
        print_book(found_contacts)
    else: # якщоконтакти не знайдені - інформація і вихід
        print_error(error_messages["no_contact"])  

# -- notes
@input_error(error_messages["no_name"])
def add_note(args, book: AddressBook):
    name = args[0]
    if book.add_note(name):
        print_success(command_messages["note_added"])

@input_error(error_messages["no_name"])
def edit_note(args, book: AddressBook):
    name = args[0]
    if book.add_note(name):
        print_success(command_messages["note_updated"])

@input_error(error_messages["no_name"])
def delete_note(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        print_error(error_messages["no_contact"])
    else:
        record.delete_note()
        print_success(command_messages["note_deleted"])

@input_error(error_messages["no_note_tag"])
def find_note_by_tag(args, book: AddressBook):
    tag = args[0]
    notes = book.find_notes_by_tag(tag)
    if not notes:
        print_hint(command_messages["no_notes_by_tag"].format(tag=tag))
        return
    
    # Notes
    tbl_header = ["Name", "Message"]
    tbl_data = [
        [note["name"], note["message"]]
        for note in notes
    ]
    tbl_data = tbl_data or ["", ""]
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_outline")
    print(str(tbl))

def find_notes(args, book: AddressBook):    
    search_term = ' '.join(args)
    notes = book.find_notes(search_term)
    if not notes:
        print_hint(command_messages["no_notes_by_string"].format(search_term=search_term))
        return
    
    # Notes
    tbl_header = ["Name", "Tag", "Message"]
    tbl_data = [
        [note["name"], note["tag"], note["message"]]
        for note in notes
    ]
    tbl_data = tbl_data or ["", "", ""]
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_outline")
    print(str(tbl))
