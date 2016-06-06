'''
r/dailyprogrammer [Easy] Challenge 34:

inputs: 3 numbers as arguments
output: the sum of the squares of the two larger numbers.

'''

def quicksort(lst_sample):
	lower = []
	greater = []
	equal = []

	if len(lst_sample) > 1:
		pivot = lst_sample[0]
		for x in lst_sample:
			if x < pivot:
				lower.append(x)
			if x > pivot:
				greater.append(x)
			if x == pivot:
				equal.append(x)
		return quicksort(lower) + equal + quicksort(greater)
	else:
		return lst_sample

def sum_squares(lst_sample):
	least = lst_sample[0]
	greatest = lst_sample[len(lst_sample)-1]
	return least**2 + greatest**2

lst_a = [7, 3, 9, 6, 5, 11, 12, 4, 2]
lst_result = quicksort(lst_a)
print sum_squares(lst_result)