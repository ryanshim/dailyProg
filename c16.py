'''
r/dailyprogrammer [Easy] Challenge 16: string character removal
Remove characters present in each other's strings
'''

def remove_char(first, second):
    temp = ''
    for x in first:
        if x not in second:
            temp += x
    print '[+] Result: ' + temp

if __name__ == '__main__':
    first = raw_input('[+] Enter first string: ')
    second = raw_input('[+] Enter second string: ')
    remove_char(first, second)
