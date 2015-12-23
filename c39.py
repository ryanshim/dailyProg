''' 
r/dailyprogrammer [Easy] Challenge 39:

do fizzbuzz
'''

def fizzbuzz(n):
	for x in range(1,n+1):
		if x % 3 == 0:
			print "fizz"
		elif x % 5 == 0:
			print "buzz"
		else:
			print x

fizzbuzz(100)