

class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.married_to = None

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_married(self, person):
        self.married_to = person
        person.married_to = self

    def is_married(self):
        return self.married_to is not None


def describe_person(person):
    print('Name: {}'.format(john.full_name()))
    print(' - Is married: {}'.format(john.is_married()))
    if john.is_married():
        print(' - Spouse: {spouse}'.format(spouse=john.married_to.full_name()))

john = Person('John', 'Doe')
jane = Person('Jane', 'Doe')

describe_person(john)
describe_person(jane)

print('-' * 30)
print('The weeding')
john.get_married(jane)

print('-' * 30)

describe_person(john)
describe_person(jane)
