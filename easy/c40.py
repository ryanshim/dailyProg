'''
r/dailyprogrammer [Easy] Challenge 40:

Write a program that will accept a sentence as input and then
output that sentence surrounded by some type of an ASCII
decoration banner.
'''

def create_banner(sentence):
    print "*"*(len(sentence) + 6)
    print "*  " + " "*(len(sentence)) + "  *"
    print "*  " + sentence + "  *"
    print "*  " + " "*(len(sentence)) + "  *"
    print "*"*(len(sentence) + 6)

sample_sentence = raw_input("Enter sentence: ")
create_banner(sample_sentence)
