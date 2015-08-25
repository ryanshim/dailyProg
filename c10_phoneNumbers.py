'''r/dailyprogrammer [Easy] Challenge 10: phone numbers
   valid formats:
            1234567890,
            123-456-7890,
            123.456.7890,
            (123)456-7890,
            (123) 456-7890,
            and 456-7890.
'''
import re
import sys

def validate_phone(num):
    if re.match('[0-9]{10}|[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{3}\.[0-9]{3}\.[0-9]{4}|\([0-9]{3}\)[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{4}', num):
        print '[+] Phone number %s is valid.' % num
    else:
        print '[+] Not a valid phone number.'
        sys.exit('[+] Terminating...')

num = raw_input('[+] Enter phone number to check for validity: ')
validate_phone(num)
