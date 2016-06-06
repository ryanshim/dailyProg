'''
r/dailyprogrammer [Easy] Challenge 30:

Write a program that takes a list of integers and a target number and 
determines if any two integers in the list sum to the target number. 
If so, return the two numbers. If not, return an indication that no such
integers exist.
'''

def find_sum(nums, target):
	for x in nums:
		for y in nums:
			if x + y is target:
				print x, y
			else:
				print "No matches"

lst_a = [1, 2, 3, 4, 5, 6]
t = 6
find_sum(lst_a, t)