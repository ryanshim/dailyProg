''' r/dailyprogrammer [Easy] Challenge 27: year characteristics'''

def find_century(y):
	century = {
				1 : list(range(1,101)),
				2 : list(range(101,201)),
				3 : list(range(201,301)),
				4 : list(range(301,401)),
				5 : list(range(401,501)),
				6 : list(range(501,601)),
				7 : list(range(601,701)),
				8 : list(range(701,801)),
				9 : list(range(801,901)),
				10 : list(range(901,1001)),
				11 : list(range(1001,1101)),
				12 : list(range(1101,1201)),
				13 : list(range(1201,1301)),
				14 : list(range(1301,1401)),
				15 : list(range(1401,1501)),
				16 : list(range(1501,1601)),
				17 : list(range(1601,1701)),
				18 : list(range(1701,1801)),
				19 : list(range(1801,1901)),
				20 : list(range(1901,2001)),
				21 : list(range(2001,2101)),
				22 : list(range(2101,2201))
				}
	for k,v in century.iteritems():
		if y in v:
			print "Century: " + str(k)

def find_leap(y):
	if y % 4 != 0:
		print "Leap Year: No"
	elif y % 100 != 0:
		print "Leap Year: Yes"
	elif y % 400 != 0:
		print "Leap Year: No"
	else:
		print "Leap Year: Yes"

year = 1996
find_century(year)
find_leap(year)