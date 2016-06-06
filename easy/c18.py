'''r/dailyprogrammer [Easy] Challenge 18: phone number convert'''

numToAlpha = {
            2: ['A', 'B', 'C'],
            3: ['D', 'E', 'F'],
            4: ['G', 'H', 'I'],
            5: ['J', 'K', 'L'],
            6: ['M', 'N', 'O'],
            7: ['P', 'Q', 'R', 'S'],
            8: ['T', 'U', 'V'],
            9: ['W', 'X', 'Y', 'Z']
            }

def convert_phone(number):
    first = number[:6]
    second = ''
    converted = ''
    for x in number[6:]:
        for k,v in numToAlpha.iteritems():
            if x in v:
                converted += str(k)
    first += converted[:3]
    second += converted[3:]
    print '[+] ' + first + '-' + second


if __name__ == '__main__':
    number = '1-800-COMCAST'
    convert_phone(number)
