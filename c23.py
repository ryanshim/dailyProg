''' 
r/dailyprogrammer [Easy] Challenge 23: List halves - if list length odd middle
item can go in any list.
'''

def halve_list(a_list):

	b_1 = []
	b_2 = []

	for i in range(len(a_list)/2):
		b_1.append(a_list[i])
	for i in range(len(a_list)/2, len(a_list)):
		b_2.append(a_list[i])

	print b_1
	print b_2
			

a = [1, 2, 3, 4, 5, 6, 7, 8]
halve_list(a)