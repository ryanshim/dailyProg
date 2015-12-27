'''
r/dailyprogrammer [Easy] Challenge 44:

Write a program that divides up some input text into sentences and
then determines which sentence in the input has the most words.
Print out the sentence with the most words and the number of words
that are in it. Optionally, also print out all words in that sentence
that are longer than 4 characters.

Sentences can end in periods, exclamation points and question marks,
but not colons or semi-colons.
'''
import re

def find_longest(text):
    sent_lengths = []
    for sentence in text:
        sent_lengths.append(len(sentence.split()))
    print (text[sent_lengths.index(max(sent_lengths))] +
          "\nWord Count = " + str(max(sent_lengths)))

f = open("c44_sample.txt", "r")
data = f.read()
f.close()
sample_text = re.findall("[A-Z][^\.!?]*[\.!?]", data)
find_longest(sample_text)
