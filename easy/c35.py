''' 
r/dailyprogrammer [Easy] Challenge 35:

Write a program that will take a number and print a right triangle attempting
to use all numbers from 1 to that number.

Sample Run:

Enter number: 10

Output:
7 8 9 10
4 5 6
2 3
1

INCOMPLETE
'''

def num_triangle():
	tri_length = input("Enter number: ")
	tri_array = [[1], [2,3], [4,5,6], [7,8,9,10]]
	for i in xrange(len(tri_array)):
		print tri_array[i]

num_triangle()