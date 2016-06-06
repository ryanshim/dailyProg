'''r/dailyprogrammer [Easy] Challenge 13: Find the number corresponding to date'''

JANUARY = range(1,32)
FEBRUARY = range(32,60)
MARCH = range(60,91)
APRIL = range(91,121)
MAY = range(121,152)
JUNE = range(152,182)
JULY = range(182,213)
AUGUST = range(213,244)
SEPTEMBER = range(244,274)
OCTOBER = range(274,305)
NOVEMBER = range(305,335)
DECEMBER = range(335,367)

months = [JANUARY,FEBRUARY,MARCH,APRIL,MAY,JUNE,JULY,AUGUST,SEPTEMBER,OCTOBER,NOVEMBER,DECEMBER]

def getnumber(m,d):
    print '[+] ' + str(m) + '-' + str(d) + ' is the ' + str(months[m-1][d-1]) + 'th day of the year.'

m = input('[+] Enter month number: ')
d = input('[+] Enter date number: ')
getnumber(m,d)
