'''r/dailyprogrammer [Easy] Challenge 1: Person Identifier'''

class person:
    def __init__(self, name, age, username):
        self.name = name
        self.age = age
        self.username = username

    def identify(self):
        print 'your name is %s, your are %s years old, and your username is %s' % (self.name, self.age, self.username)

if __name__ == '__main__':
    name = raw_input('Enter your name: ')
    age = raw_input('Enter your age: ')
    username = raw_input('Enter your username: ')

    new_person = person(name, age, username)
    new_person.identify()
