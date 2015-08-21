'''r/dailyprogrammer [Easy] Challenge 5: password protected'''
import sys
import hashlib
import getpass # hides password inputs

def main(argv):
    pass_file = open(argv)
    password = pass_file.readline()[:-1]
    pass_file.close()

    pass_try = ''

    if len(password) > 0:
        pass_try = hashlib.sha256(getpass.getpass('Enter password: ')).hexdigest()
        if pass_try == password:
            print '[+] Access Granted.'
        else:
            sys.exit('[+] Access Denied.\n[+] Terminating process.')
    else:
        sys.exit('[+] No password set.')

if __name__ == '__main__':
    main(sys.argv[1])
