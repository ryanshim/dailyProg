'''r/dailyprogrammer [Easy] Challenge 17: triangles'''

def triangle(height):
    for x in range(height):
        print '*' * x
    for x in reversed(range(height)):
        print '*' * x

if __name__ == '__main__':
    height = input('[+] Enter triangle height: ')
    triangle(height)
