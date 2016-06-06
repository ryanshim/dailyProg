'''r/dailyprogrammer [Easy] Challenge 11: calendar day'''

import datetime

date = input('Enter the date: ')
month = input('Enter the month: ')
year = input('Enter the year: ')

mydate = datetime.date(year, month, date)
print mydate.strftime('%A')
