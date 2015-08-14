'''r/dailyprogrammer [Easy] Challenge 3: rot13 encryption'''

origin_table = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
encoded = {}
i = 0

for char in origin_table:
    encoded[i] = char
    i += 1

def encode():
    msg = raw_input('Enter message to encrypt: ')
    temp = msg.upper()
    for char in temp:
        current = origin_table.index(char)
        print current

print encode()
