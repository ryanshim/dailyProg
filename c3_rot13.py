'''r/dailyprogrammer [Easy] Challenge 3: rot13 encryption'''

char_list = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'

def encode():
    msg = raw_input('Enter message to encrypt: ')
    encoded = []
    for char in msg.upper():
        rot13 = (char_list.index(char) + 13) % 26
        encoded += char_list[rot13]
    return ''.join(encoded)

print encode()