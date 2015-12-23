''' r/dailyprogrammer [Easy] Challenge 22: missing list values'''

def add_values(a, b):
	for x in b:
		if x not in a:
			a.append(x)
	print a

lst_1 = ["a","b","c",1,4,]
lst_2 = ["a", "x", 34, "4"]
add_values(lst_1, lst_2)