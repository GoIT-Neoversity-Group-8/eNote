from utils.error_handlers import input_error
from constants.messages import error_messages, command_messages
from app.AddressBook import AddressBook
from utils.validators import *
from utils.print_handlers import *
from tabulate import tabulate
from app.Record import Record

def bot_hello(args, book: AddressBook):
    print_hint(command_messages["hello"])

# -- Contact
@input_error(error_messages["no_name"])
def add_contact(args, book: AddressBook):
    name = args[0]
    book.add_contact(name)
    print_success(command_messages["contact_added"])

@input_error(error_messages["no_name"])
def update_contact(args, book: AddressBook):
    name = args[0]
    book.update_contact(name)
    print_success(command_messages['contact_updated'].format(name=name))

@input_error(error_messages["no_name"])
def delete_contact(args, book: AddressBook):
    name = args[0]
    if book.delete_contact(name):
        print_success(command_messages['contact_deleted'].format(name=name))
    else:
        print_error(error_messages["no_contact"])

def show_all(args, book: AddressBook):
    if not book.data:
        print(error_messages["no_contacts"])
        return
    # Таблиця контактів
    tbl_header = ["Name", "Phone", "Birthday", "Email", "Address", "Note"]
    tbl_data = [
        [
            record.name, 
            "\n".join(list(map(str, record.phones))), 
            str(record.birthday), 
            str(record.email), 
            str(record.address), 
            str(record.note)
        ]
        for name, record in book.data.items()
    ]
    tbl_data = tbl_data or ["", "", "", "", "", ""]
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_grid")
    print(str(tbl))

# -- Phones
@input_error(error_messages["no_name_and_phone"])
def add_phone(args, book: AddressBook):
    name, phone = args
    if book.add_phone(name, phone):
        print_success(command_messages["phone_added"])

@input_error()
def delete_phone(args, book: AddressBook):
    try:
        name, phone_to_del = args
    except:
        raise ValueError(error_messages["no_name_and_phone"])
    
    if book.delete_phone(name, phone_to_del):
        print_success(command_messages['phone_deleted'].format(name=name, phone=phone_to_del))
    else:
        print_error(error_messages["no_contact"])

@input_error()
def show_phones(args, book: AddressBook):
    try:
        name = args[0]
    except:
        raise ValueError(error_messages["no_name"])
    
    phones = book.show_phones(name)
    if phones:
        txt_phones = ", ".join(map(str, phones))
        mess = command_messages['show_phones'].format(name=name)
        print_hint(f"{mess}: {txt_phones}")
    else:
        print_error(error_messages["no_phones"])

# -- Birthdays
@input_error(error_messages["no_name_and_birthday"])
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        print_error(error_messages["no_contact"])
    elif record.add_birthday(birthday):
        print_success(command_messages["birthday_added"])

@input_error(error_messages["no_name"])
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        print_error(error_messages["no_contact"])
    elif record.birthday and record.birthday.value:
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

@input_error(error_messages["no_name"])
def find_contact(args, book: AddressBook):
    search_term = ' '.join(args) #передані параметри вважаємо одним рядком і шукаємо по ньому
    found_contacts = book.find_contact(search_term)
    if found_contacts: # якщо список знайдених не порожній - показуємо таблицю з результатами
        tbl_header = ["Name", "Phone", "Email", "Address", "Birthday", "Note"]
        tbl_data = [
            [
                record.name, 
                "\n".join(list(map(str, record.phones))), 
                str(record.birthday), 
                str(record.email), 
                str(record.address), 
                str(record.note)
            ] 
            for name, record in found_contacts.items()
        ]
        tbl_data = tbl_data or ["", "", "", "", "", ""]
        tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_grid")
        print(str(tbl))
    else: # якщоконтакти не знайдені - інформація і вихід
        print_error(error_messages["no_contact"])  

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
        return
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
