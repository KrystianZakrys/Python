import re

def get_email():
    return input("Please enter your email address: ")


def email_validate(email):
    regex = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', flags=re.IGNORECASE)
    if len(email) > 7:
        if regex.match(email):
            return True
        else:
            return False
    else:
        return False

email = get_email()
if not email_validate(email):
    raise NotImplementedError("Invalid email!")
else:
    print("Your email ",email," is VALID!")
