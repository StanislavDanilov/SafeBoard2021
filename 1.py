import re


def check_password(password):
    if re.match(r'[A-Za-z0-9\'\"!#$%&’()*+,-./:;<=>?@\[\]^_`{|}~.]{10,}', password) \
            and len(set(password)) > 5 and "kaspersky" not in password.lower():
        return "GOOD"
    else:
        return "BAD"


print(check_password(input("")))
