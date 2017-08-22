import sys
sys.path.append("..")
from address_terminal.models.entry import Entry

class AddressBook(object):
    def __init__(self, entries = []):
        self.entries = entries

    def add_entry(self, name, phone_number, email):
        index = 0
        for entry in self.entries:
            if name < entry.name: break
            index += 1

        self.entries.insert(index, Entry(name, phone_number, email))
