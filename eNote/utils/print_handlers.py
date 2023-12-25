"""Print utils."""
from tabulate import tabulate
# from eNote.app.AddressBook import AddressBook

RED = "\033[91m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"


def print_error(msg):
    """Print errors."""
    print(RED + str(msg) + RESET)


def print_command(msg):
    """Print commands."""
    print(CYAN + str(msg) + RESET)


def print_subcommand(msg):
    """Print subcommands."""
    print(BLUE + str(msg) + RESET)


def print_success(msg):
    """Print success results."""
    print(GREEN + str(msg) + RESET)


def print_hint(msg):
    """Print hints."""
    print(ORANGE + str(msg) + RESET)

def format_text_width(text, width = 20):
    """Formats the string length to [width].
    
    The result is a multi-line variable with \\n characters.
    The line width is set to [width] = 20
    """
    if not text:
        return None
    text = str(text)
    words = text.split()
    current_line = ""
    formated_lines = []
    for word in words:
        if len(current_line + word) <= width:
            current_line += word + " "
        else:
            formated_lines.append(current_line.strip())
            current_line = word + " "
    formated_lines.append(current_line.strip())
    formated_text = "\n".join(formated_lines)
    return formated_text



def print_book(book):
    """Print AddressBook as a table.
    book: AddressBook"""
    # Таблиця контактів
    tbl_header = ["Name", "Phone", "Birthday", "Email", "Address", "Note"]
    tbl_data = [
        [
            record.name,
            "\n".join(list(map(str, record.phones))),
            record.birthday,
            record.email,
            format_text_width(record.address,30),
            format_text_width(record.note, 30),
        ]
        for name, record in book.data.items()
    ]
    tbl_data = tbl_data or [
        "" for _ in tbl_header
    ]  # якщо даних немає - порожні клітинки
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_grid")
    print(str(tbl))
