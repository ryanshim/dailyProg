''' r/dailyprogrammer [Easy] Challenge 29: palindromes'''

def palindrome(a_string):
	if len(a_string) % 2 == 0:
		first, second = a_string[:len(a_string)/2], a_string[len(a_string)/2:]
		if first[::-1] == second:
			print "Palindrome"
		else:
			print "Not Palindrome"
	else:
		first, second = a_string[:len(a_string)/2], a_string[(len(a_string)/2)+1:]
		if first[::-1] == second:
			print "Palindrome"
		else:
			print "Not Palindrome"

sample_a = "hannah"
sample_b = "12321"
sample_c = "123210"

palindrome(sample_a)
palindrome(sample_b)
palindrome(sample_c)