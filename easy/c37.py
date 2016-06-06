''' 
r/dailyprogrammer [Easy] Challenge 37:

write a program that takes
input : a file as an argument
output: counts the total number of lines.
for bonus, also count the number of words in the file.

'''

def line_count(f_name):
	f = open(f_name, "r")
	lines = f.read()
	result = 0
	for character in lines:
		if character == "\n":
			result += 1
	print "Line Count: " + str(result)

line_count("c37_sample.txt")