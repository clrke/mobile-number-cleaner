import re

PHILIPPINE_COUNTRY_CODES = ['+63']

def clean(mobile_number):
    if len(mobile_number) == 0:
        return None

    mobile_number_with_plus = (
            mobile_number
            if mobile_number[0] == '+'
            else '+' + mobile_number
    )

    mobile_number_without_spaces = re.sub(r'\s', '', mobile_number_with_plus)

    index_of_parenthesis = mobile_number_without_spaces.index('(')
    country_code = mobile_number_without_spaces[:index_of_parenthesis]

    mobile_number_without_parentheses = re.sub(r'[()]', '', mobile_number_without_spaces)

    philippine_number = (
            country_code in PHILIPPINE_COUNTRY_CODES
            or re.match(r'\+0+', country_code)
    )

    if not philippine_number:
        return mobile_number_without_parentheses

    return '+63' + mobile_number_without_parentheses[-10:]

