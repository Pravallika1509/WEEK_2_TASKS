import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

print(is_valid_email("user@domain.com"))
print(is_valid_email("user@domain"))