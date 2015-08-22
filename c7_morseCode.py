'''r/dailyprogrammer [Easy] Challenge 7: morse code'''

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
            ' ': ' / '
            }

def encode(msg):
    encrypted = []
    for k in msg.upper():
        if k in morse_alpha:
            encrypted.append(morse_alpha[k])
    print ''.join(encrypted)

if __name__ == '__main__':
    enc_dec = raw_input('[+] Enter message to encode: ')
    encode(enc_dec)
