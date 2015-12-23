''' r/dailyprogrammer [Easy] Challenge 26: string duplicates'''

def filter_string(a_string):
	found = []
	dupes = []
	for letter in a_string:
		if letter not in found:
			found.append(letter)
		else:
			dupes.append(letter)
	print "".join(found),
	print "".join(dupes)

some_string = "balloons"
filter_string(some_string)