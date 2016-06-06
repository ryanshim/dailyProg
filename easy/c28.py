''' r/dailyprogrammer [Easy] Challenge 28: finding array duplicates'''

def find_duplicate(some_list):
	for i in range(len(some_list)):
		for j in range(i+1, len(some_list)):
			if some_list[i] == some_list[j]:
				print "Duplicate found at index %d and index %d" % (i,j)


	#for x in some_list:
	#	if some_list.count(x) >= 2:
	#		print x

lst_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6]
find_duplicate(lst_a)