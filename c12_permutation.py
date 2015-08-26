'''r/dailyprogrammer [Easy] Challenge 12: permutations:
find all permutations of the string hi!'''

import itertools

a_string = 'hi!'
for x in itertools.permutations(a_string, 3):
    print ''.join(x),
