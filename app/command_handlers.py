from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages, command_messages
from app.AddressBook import AddressBook

def bot_hello(args, book: AddressBook):
    print(command_messages["hello"])

@input_error(error_messages["no_name"])
def add_contact(args, book: AddressBook):
    name = args[0]
    # TODO implementation 
    print(command_messages["contact_added"])

@input_error(error_messages["no_name_and_phone"])
def add_phone(args, book: AddressBook):
    name, phone = args
    # TODO implementation 
    print(command_messages["phone_added"])

@input_error(error_messages["no_name"])
def show_phones(args, book: AddressBook):    
    name = args[0]
    # TODO implementation 
    print(f"Phones number for {name}: xxxxxxxxxx, xxxxxxxxxx")

def show_all(args, book: AddressBook):
    # TODO implementation 
    print("All data")

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
