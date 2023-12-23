"""Print utils."""
from tabulate import tabulate
# from app.AddressBook import AddressBook

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
            record.address,
            record.note,
        ]
        for name, record in book.data.items()
    ]
    tbl_data = tbl_data or [
        "" for _ in tbl_header
    ]  # якщо даних немає - порожні клітинки
    tbl = tabulate(tbl_data, tbl_header, tablefmt="rounded_grid")
    print(str(tbl))
