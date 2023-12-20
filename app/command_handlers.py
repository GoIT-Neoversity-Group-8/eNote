from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages, command_messages, validation_messages
from app.AddressBook import AddressBook
from utils.validators import *
from tabulate import tabulate
from app.Record import Record


def bot_hello(args, book: AddressBook):
    print(command_messages["hello"])


@input_error(error_messages["no_name"])
def add_contact(args, book: AddressBook):
    name = args[0]
    # TODO implementation
    book.add_contact(name)
    print(command_messages["contact_added"])


@input_error(error_messages["no_name_and_phone"])
def add_phone(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError()
    name, phone = args
    if not is_valid_phone(phone):
        raise ValueError(validation_messages["invalid_phone"])
    book.add_phone(name, phone)
    print(command_messages["phone_added"])


@input_error(error_messages["no_name"])
def show_phones(args, book: AddressBook):
    name = args[0]
    # TODO implementation
    print(f"Phones number for {name}: xxxxxxxxxx, xxxxxxxxxx")


def show_all(args, book: AddressBook):
    # TODO implementation
    print("All data")
    # if not book.data:
    #     print(error_messages["no_contacts"])
    #     return

    # Таблиця контактів
    tbl_header = ["Name", "Phone", "Email", "Address", "Birthday", "Note"]
    tbl_data = [
        [record.name, ",".join(map(str, record.phones))]
        for name, record in book.data.items()
    ]
    tbl_data = tbl_data or ["", "", "", "", "", ""]
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_outline")
    print(str(tbl))


@input_error(error_messages["no_name_and_birthday"])
def add_birthday(args, book: AddressBook):
    name, birthday = args
    # TODO implementation
    print(command_messages["birthday_added"])


@input_error(error_messages["no_name"])
def show_birthday(args, book: AddressBook):
    name = args[0]
    # TODO implementation
    print(f"Birthday for {name}: DD.MM.YYYY")

@input_error(error_messages["no_name"])
def show_birthdays(args, book: AddressBook):
    # TODO implementation 
    print("Show_birthdays")

@input_error(error_messages["no_name"])
def find_birthdays(args, book: AddressBook):
    # TODO implementation 
    days = int(args[0])
    print(f"Show_birthdays during {days}")

@input_error(error_messages["no_name"])
def find_contact(args, book: AddressBook):
    # TODO implementation
    search_term = ' '.join(args)
    print(f"Find contact by {search_term}")  

@input_error(error_messages["no_name_and_note_data"])
def add_note(args, book: AddressBook):
    if len(args) <= 2:
        raise ValueError()
    name, tag, *note = args
    record = book.find(name)
    if not record:
        print(f"Contact {name} not found.")
        return
    msg = ' '.join(note)
    record.add_note(tag, msg)
    print(f"Note added for {name} with tag {tag}")

@input_error(error_messages["no_name_and_note_data"])
def edit_note(args, book: AddressBook):
    if len(args) <= 2:
        raise ValueError()
    name, tag, *note = args
    record = book.find(name)
    if not record:
        print(f"Contact {name} not found.")
        return
    msg = ' '.join(note)
    record.add_note(tag, msg)
    print(f"Note updated for {name} with tag {tag}")

@input_error(error_messages["no_name"])
def delete_note(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError()
    name = args[0]
    record = book.find(name)
    if not record:
        print(f"Contact {name} not found.")
        return
    record.delete_note()
    print(f"Note deleted for contact {name}")

@input_error(error_messages["no_note_tag"])
def find_note_by_tag(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError()
    tag = args[0]
    notes = book.find_notes_by_tag(tag)
    if not notes:
        print(f"Notes with tag '{tag}' not found.")
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
        print(f"Notes with search term '{search_term}' not found.")
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

@input_error(error_messages["no_name"])
def update_contact(args, book: AddressBook):
    # TODO implementation 
    name, phone, birthday, email, address = args
    print(f"Update {name}")

@input_error(error_messages["no_name"])
def delete_contact(args, book: AddressBook):    
    # TODO implementation 
    name = args[0]
    print(f"Delete {name}")

