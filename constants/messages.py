# -- Custom error messages
error_messages = {
    "invalid_command": "Invalid command. Use 'help' command for Help!",
    "no_command": "Enter some command please.",
    "no_name": "Give me name please.",
    "no_name_and_phone": "Give me name and phone please.",
    "no_name_and_phones": "Give me name, phone to update and new phone please.",
    "no_contact": "There is no such contact in your phone book.",
    "no_contacts": "There are no contacts in your phone book yet.",
    "no_name_and_birthday": "Give me name and birthday please.",
}

# -- Validation error messages
validation_messages = {
    "invalid_phone": "The phone entered is not valid.",
    "invalid_date": "The date entered is not valid.",
    "invalid_email": "The email entered is not valid.",
}

# -- User helpers for commands
command_messages = {
    "welcome": "Welcome to the assistant bot!",
    "commands":  "\nAvailable commands:",
    "enter_command": "Enter a command: ",
	"hello": "Hello,/nHow can I help you?",
    "contact_added": "Contact added",
    "phone_added": "Phone added",
    "email_added": "Email added",
    "birthday_added": "Birthday added",
    "note_added": "Tag added",
    "good_bye": "Good bye!",
}

# -- Help table column headers
help_table_messages = {
    "command_col": "Command",
    "example_col": "Example with arguments",
    "description_col": "Description",  
}

# -- Help table command descriptions
command_descriptions = {
    "help": "Shows a list of available commands with descriptions.",
    "hello": "Greets the user.",
    "exit": "Exits the program.",
    "show_all": "Show all contacts, ordered by name",
    "add_contact": "Add new contact name",
    "add_phone": "Add new phone (10-digits number) for contact by name",
    "show_phones": "Show phones for contact by name",
    "add_birthday": "Add birthday (DD.MM.YYYY) for contact by name",
    "show_birthday": "Show birthday for contact by name",
}
