'''r/dailyprogrammer [Easy] Challenge 6: Pi'''
import math
from decimal import *

def main(pi):
    places = input('[+] Enter decimal precision: ')
    getcontext().prec = places + 1
    print Decimal(pi) + Decimal(0.0)

if __name__ == '__main__':
    main(math.pi)
