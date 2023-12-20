from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages, command_messages, validation_messages
from app.AddressBook import AddressBook
from utils.validators import *
from tabulate import tabulate


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
  

@input_error(error_messages["no_name"])
def add_note(args, book: AddressBook):
    # TODO implementation 
    name = args[0]
    note = ' '.join(args[1:])
    print(f"Note added to {name}: {note}")

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

