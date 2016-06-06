'''r/dailyprogrammer [Easy] Challenge 7: morse code'''
import sys

morse_alpha = {
            'A': '.-',      'B': '-...',
            'C': '-.-.',    'D': '-..',
            'E': '.',       'F': '..-.',
            'G': '--.',     'H': '....',
            'I': '..',      'J': '.---',
            'K': '-.-',     'L': '.-..',
            'M': '--',      'N': '-.',
            'O': '---',     'P': '.--.',
            'Q': '--.-',    'R': '.-.',
            'S': '...',     'T': '-',
            'U': '..-',     'V': '...-',
            'W': '.--',     'X': '-..-',
            'Y': '-.--',    'Z': '--..',
            ' ': ' / ',     ' ': '/'
            }

def encode(msg):
    encrypted = []
    for k in msg.upper():
        if k in morse_alpha:
            encrypted.append(morse_alpha[k])
    print '\n[+] ' + ''.join(encrypted) + '\n'

def decode(msg):
    decoded = []
    letters = msg.split(' ')
    for i in letters:
        for k,v in morse_alpha.items():
            if i == v:
                decoded.append(k)
    print '\n[+] ' + ''.join(decoded) + '\n'

if __name__ == '__main__':
    enc_dec = input('[+] 1 = Encrypt, 2 = Decrypt: ')
    if enc_dec == 1:
        msg = raw_input('[+] Enter message to encode: ')
        encode(msg)
    elif enc_dec == 2:
        msg = raw_input('[+] Enter message to decode: ')
        decode(msg)
    else:
        sys.exit('[+] Wrong input\n[+] Terminating...')
