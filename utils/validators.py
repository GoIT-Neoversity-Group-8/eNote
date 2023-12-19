from datetime import datetime
import re

phone_pattern = re.compile(r'\d{10}')
email_pattern = re.compile(r'') # TODO find regex for emails
date_format_default = '%d.%m.%Y'

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, date_format_default)
        return True
    except ValueError:
        return False

def is_valid_phone(phone):
	return bool(phone_pattern.match(phone))

def is_valid_email(email):
    return bool(email_pattern.match(email))
