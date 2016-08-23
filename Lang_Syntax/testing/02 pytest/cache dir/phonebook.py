import os

class Phonebook:

    
    def __init__(self, cachedir):
        self.contacts = {}
        self.filename = "phonebook.txt"
        self.consistent = True
        self.file_cache = open(os.path.join(str(cachedir), self.filename), "w")


    def add(self, name, number):
        self.contacts[name] = number


    def lookup(self, name):
        assert name != None, "name parameter is required!"
        return self.contacts[name]


    def names(self):
        return set(self.contacts.keys())


    def numbers(self):
        return set(self.contacts.values())


    def is_consistent():
        return self.consistent

    def clear(self):
        self.entries = {}
        self.file_cache.close()
        os.remove(self.filename)
