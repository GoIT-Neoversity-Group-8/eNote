RED = "\033[91m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

def print_error(msg):
	print(RED + msg + RESET)

def print_command(msg):
	print(CYAN + msg + RESET)

def print_subcommand(msg):
	print(BLUE + msg + RESET)

def print_success(msg):
	print(GREEN + msg + RESET)

def print_hint(msg):
	print(ORANGE + msg + RESET)
