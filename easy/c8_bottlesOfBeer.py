'''r/dailyprogrammer [Easy] Challenge 8: bottles of beer'''

def beer_song(bottle_count):
    while bottle_count > 0:
        print ' ' + str(bottle_count) + ' bottles of beer on the wall, ' + str(bottle_count) + ' bottles of beer, take one down, pass it around, ',
        bottle_count -= 1
        print str(bottle_count) + ' bottles of beer on the wall.',

if __name__ == '__main__':
    bottle_count = input('How many bottles of beer are on the wall: ')
    beer_song(bottle_count)
