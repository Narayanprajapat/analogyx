import re


def match_value(value, regex):
    if re.match(regex, value):
        return True
    else:
        return False
