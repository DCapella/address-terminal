from entry import Entry

class AddressBook(object):
    """
    Creating a new Address Book object
    """
    def __init__(self, entries = []):
        """
        Inititalize object with attribute entries
        """
        self.entries = entries

    def add_entry(self, name, phone_number, email):
        """
        Giving object the attribute to add entries
        """
        index = 0
        for item in self.entries:
            if name < item.name: break
            index += 1

        self.entries.insert(index, Entry(name, phone_number, email))
