from utils.error_handlers import input_error
from constants.messages import error_messages, command_messages
import shlex

@input_error(error_messages["no_command"])
def parse_input(user_input):
    # cmd, *args = user_input.split()
    cmd, *args = shlex.split(user_input)
    cmd = cmd.strip().lower()
    return cmd, *args
