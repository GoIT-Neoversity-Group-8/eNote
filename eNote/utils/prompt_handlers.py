ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

def is_yes_prompt(msg):
    user_answer = input(ORANGE + msg + RESET)
    return user_answer.lower() in ["yes", "y"]
