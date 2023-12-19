from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages
from app.AddressBook import AddressBook

def bot_hello(args, book:AddressBook):
    return "Hello,/nHow can I help you?"

def add_contact(args, book:AddressBook):
    name = args[0]
    # TODO implementation 
    print("Contact added.")

def add_phone(args, book:AddressBook):
    name, phone = args
    # TODO implementation 
    print("Phone added.")

def show_phones(args, book:AddressBook):    
    name = args[0]
    # TODO implementation 
    print(f"Phones number for {name}: xxxxxxxxxx, xxxxxxxxxx")
    
def show_all(args, book:AddressBook):
    # TODO implementation 
    print("All data")

def add_birthday(args, book:AddressBook):
    name, birthday = args
    # TODO implementation 
    print("Birthday added")

def show_birthday(args, book:AddressBook):
    name = args[0]
    # TODO implementation 
    print(f"Birthday for {name}: DD.MM.YYYY")