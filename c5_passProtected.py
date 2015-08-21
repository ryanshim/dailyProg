'''r/dailyprogrammer [Easy] Challenge 5: password protected'''
import sys
import hashlib
import getpass # hides password inputs

def main(argv):
    pass_file = open(argv)
    password = pass_file.readline()[:-1]
    pass_file.close()

    if len(password) > 0:
        pass_try = hashlib.sha256(getpass.getpass('[+] Enter password: ')).hexdigest()
        if pass_try == password:
            print '[+] Access Granted.'
            # go to another function after login
        else:
            sys.exit('[+] Access Denied.\n[+] Terminating process.')
    else:
        set_pass(argv)

def set_pass(argv):
    pass_file = open(argv, 'w')
    pass_file.write(hashlib.sha256(getpass.getpass('[+] Enter new password: ')).hexdigest() + '\n') # need a newline due to line 8 readline
    pass_file.close()
    return main(argv)

if __name__ == '__main__':
    main(sys.argv[1])
