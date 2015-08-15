'''r/dailyprogrammer [Easy] Challenge 3: rot13 encryption'''

origin_table = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'

def encode():
    msg = raw_input('Enter message to encrypt: ')
    temp = msg.upper()
    encoded = []
    for char in temp:
        rot13 = (origin_table.index(char) + 13) % 26
        encoded += origin_table[rot13]
    print ''.join(encoded)

print encode()
