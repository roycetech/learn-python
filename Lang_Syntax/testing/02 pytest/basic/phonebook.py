class Phonebook:

    
    def __init__(self):
        self.contacts = {}
        self.consistent = True


    def add(self, name, number):
        self.contacts[name] = number


    def lookup(self, name):
        assert name != None, "name parameter is required!"
        return self.contacts[name]


    def names(self):
        return set(self.contacts.keys())


    def is_consistent():
        return self.consistent
