'''r/dailyprogrammer [Easy] Challenge 4: random password gen'''

import random

char = 'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
charlist = []

pass_len = input('Enter desired password length: ')
pass_gen = []
charlist += char

for i in range(pass_len):
    pass_gen.append(random.choice(charlist))
print ''.join(pass_gen)
